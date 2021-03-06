# -*- coding: utf-8-*-
from robot import ASR, TTS, AI, Player, config, constants, utils
from robot.Brain import Brain
from snowboy import snowboydecoder
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Conversation(object):

    def __init__(self):
        self.player = None
        self.brain = Brain(self)
        self.reload()
        self.history = []

    def interrupt(self):
        if self.player is not None and self.player.is_playing():
            self.player.stop()
            self.player = None

    def reload(self):
        """ 重新初始化 """
        try:
            self.asr = ASR.get_engine_by_slug(config.get('asr_engine', 'tencent-asr'))
            self.ai = AI.get_robot_by_slug(config.get('robot', 'tuling'))
            self.tts = TTS.get_engine_by_slug(config.get('tts_engine', 'baidu-tts'))
        except Exception as e:
            logger.critical("对话初始化失败：{}".format(e))

    def _doResponse(self, query):
        self.appendHistory(0, query)        
        if not self.brain.query(query):
            # 没命中技能，使用机器人回复
            msg = self.ai.chat(query)
            self.say(msg, True)

    def converse(self, fp):
        """ 核心对话逻辑 """
        try:
            self.interrupt()
            snowboydecoder.play_audio_file(constants.getData('beep_lo.wav'))
            query = self.asr.transcribe(fp)
            utils.check_and_delete(fp)
            self._doResponse(query)
        except Exception as e:
            logger.critical(e)
            utils.clean()

    def appendHistory(self, t, text):
        """ 将会话历史加进历史记录 """
        if t in (0, 1) and text != '':
            self.history.append({'type': t, 'text': text})

    def _onCompleted(self, msg):
        if msg.endswith('?') or msg.endswith(u'？') or \
           u'告诉我' in msg or u'请回答' in msg:
            query = self.activeListen()
            self._doResponse(query)            

    def say(self, msg, cache=False, plugin='', onCompleted=None):
        """ 说一句话 """
        if plugin != '':
            self.appendHistory(1, "[{}] {}".format(plugin, msg))
        else:
            self.appendHistory(1, msg)
        voice = ''
        if utils.getCache(msg):
            logger.info("命中缓存，播放缓存语音")
            voice = utils.getCache(msg)
        else:
            voice = self.tts.get_speech(msg)
            if cache:
                utils.saveCache(voice, msg)
        if onCompleted is None:
            onCompleted = lambda: self._onCompleted(msg)
        self.player = Player.SoxPlayer()
        self.player.play(voice, not cache, onCompleted)

    def activeListen(self, MUSIC=False):
        """ 主动问一个问题(适用于多轮对话) """
        snowboydecoder.play_audio_file(constants.getData('beep_hi.wav'))
        listener = snowboydecoder.ActiveListener([constants.getHotwordModel(config.get('hotword', 'wukong.pmdl'))])
        voice = listener.listen()
        snowboydecoder.play_audio_file(constants.getData('beep_lo.wav'))
        query = self.asr.transcribe(voice)
        utils.check_and_delete(voice)
        return query    
