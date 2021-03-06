# wukong-robot

wukong-robot 是一个简单灵活的中文语音对话机器人。

## Table of Contents

* [开发进度](#研发进度)
* [特性](#特性)
* [硬件要求](#硬件要求)
* [安装](#安装)
* [升级](#升级)
* [运行](#运行)
* [配置](#配置)
* [技能插件](#插件)
* [贡献](#贡献)
* [联系](#联系)
* [感谢](#感谢)
* [FAQ](#faq)
* [免责声明](#免责声明)

## 特性

* 模块化。功能插件、语音识别、语音合成、对话机器人都做到了高度模块化，第三方插件单独维护，方便继承和开发自己的插件。
* 中文支持。集成百度、科大讯飞、阿里、腾讯等多家中文语音识别和语音合成技术，且可以继续扩展。
* 对话机器人支持。支持接入图灵机器人、Emotibot 等对话机器人。
* 全局监听，离线唤醒。支持无接触地离线语音指令唤醒。
* 灵活可配置。支持定制机器人名字，支持选择语音识别和合成的插件。
* 智能家居。支持和 mqtt、HomeAssistant 等智能家居协议联动，支持语音控制智能家电。
* 后台配套支持。提供配套后台，可实现远程操控和修改配置（开发中，进度见[这里](https://github.com/wzpan/wukong-robot/wiki/roadmap)）。
* 安装简单，支持更多平台。相比 dingdang-robot ，舍弃了 PocketSphinx 的离线唤醒方案，安装变得更加简单，代码量更少，更易于维护并且能在 Mac 以及更多 Linux 系统中运行。

## 硬件要求 ##

wukong-robot 支持运行在以下的设备和系统中：

* 64bit Mac OS X
* 64bit Ubuntu（12.04 and 14.04）
* 全系列的树莓派（Raspbian 系统）
* Pine 64 with Debian Jessie 8.5（3.10.102）
* Intel Edison with Ubilinux （Debian Wheezy 7.8）

## 安装 ##

见 [wukong-robot 安装教程](https://github.com/wzpan/wukong-robot/wiki/install) 。

## 升级

``` bash
python wukong.py update
```

如果提示升级失败，可以尝试在 wukong-robot 的根目录手动执行以下命令，看看问题出在哪。

``` sh
git pull
pip install -r requirements.txt
```

## 运行 ##

``` bash
python wukong.py
```

建议在 [tmux](http://blog.jobbole.com/87278/) 或 supervisor 中执行。

第一次启动时将提示你是否要到用户目录下创建一个配置文件，输入 `y` 即可。

然后通过唤醒词 “孙悟空” 唤醒 wukong-robot 进行交互（该唤醒词可自定义）。

要让 wukong-robot 暂时屏蔽离线监听，可以使用热词 “悟空别吵”；要让 wukong-robot 恢复离线监听，可以使用热词 “悟空醒醒”。

## 配置 ##

参考[配置文件的注释](https://github.com/wzpan/wukong-robot/blob/master/static/default.yml)进行配置即可。注意不建议直接修改 default.yml 里的内容，否则会给后续通过 `git pull` 更新带来麻烦。你应该拷贝一份放到 `$HOME/.wukong/config.yml` 中，或者在运行的时候按照提示让 wukong-robot 为你完成这件事。

几个 tips：

1. 建议在运行 wukong-robot 的机器上重新训练一下唤醒词，不同设备录制出来的唤醒词模型使用效果会大打折扣。
2. 不论使用哪个厂商的API，都建议注册并填上自己注册的应用信息，而不要用默认的配置。这是因为这些API都有使用频率和并发数限制，过多人同时使用会影响服务质量。

## 技能插件 ##

* [官方插件列表](https://github.com/wzpan/wukong-robot/wiki/plugins)
* [用户贡献插件](https://github.com/wzpan/wukong-contrib)

## 贡献

* 喜欢本项目请先打一颗星；
* 提 bug 请到 [issue 页面](https://github.com/wzpan/wukong-robot/issues)；
* 要贡献代码，欢迎 fork 之后再提 pull request；
* 插件请提交到 [wukong-contrib](https://github.com/wzpan/wukong-contrib) ；
* 您的捐赠将鼓励我继续完善 wukong-robot，支持支付宝、微信等捐赠形式。

| 支付宝 | 微信支付 |
| ------ | --------- |
| <img src="http://hahack.com/images/misc/alipay.png" height="248px" width="164px" title="支付宝" style="display:inherit;"/> | <img src="http://hahack.com/images/misc/wechatpay.jpeg" height="248px" width="164px" title="微信支付" style="display:inherit;"/> |


## 联系

* wukong-robot 的主要开发者是 [潘伟洲](http://hahack.com) 。
* QQ 群：580447290（人数将满，为控制人数，需付费20元入群）
* 论坛：[bbs.hahack.com](http://bbs.hahack.com)

## 感谢

* 悟空的前身是 [dingdang-robot](https://github.com/dingdang-robot/dingdang-robot) 项目和 [jasper-client](https://github.com/jasperproject/jasper-client) 项目。感谢 [Shubhro Saha](http://www.shubhro.com/), [Charles Marsh](http://www.crmarsh.com/) and [Jan Holthuis](http://homepage.ruhr-uni-bochum.de/Jan.Holthuis/) 在 Jasper 项目上做出的优秀贡献；

## FAQ

- 我能否更换成其他唤醒词，而不是叫“孙悟空”？

  - 能。到 [snowboy官网](http://snowboy.kitt.ai/) 训练一个自己的唤醒词，然后将生成的 pmdl 文件放到 ~/.wukong 中，然后修改配置文件中的 `hotword` 配置即可。

## 免责声明

* wukong-robot 只用作个人学习研究，如因使用 wukong-robot 导致任何损失，本人概不负责。
* 本开源项目与腾讯叮当助手及优必选悟空项目没有任何关系。
