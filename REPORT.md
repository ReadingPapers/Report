![image](https://github.com/ReadingPapers/Report/assets/56926538/ddc7f3fb-d1f2-456a-b39e-b3b94d72d191)

> 按照一下格式介绍分享的paper，定期归类整理！  
内容包含：标题, 相关连接(pdf,code，silde), 一段话介绍，主要模型框架图


**---------------------------------目录-----------------------------**

<!-- TOC -->
  * [Deep Learning](#deep-learning)
    * [PETL: parameters effective transfer learning](#petl-parameters-effective-transfer-learning)
    * [MTL，multi-task learning](#mtlmulti-task-learning)
    * [MoE, Mixture of Experts](#moe-mixture-of-experts)
  * [NLP](#nlp)
  * [CV](#cv)
    * [<font color=Green> Facial expression recognition</font>](#font-colorgreen-facial-expression-recognitionfont)
  * [Multimodality](#multimodality)
  * [Embodied AI](#embodied-ai)
    * [<font color=Green> Navigation </font>](#font-colorgreen-navigation-font-)
      * [Visual language navigation](#visual-language-navigation)
    * [<font color=Green> Manipulate </font>](#font-colorgreen-manipulate-font-)
    * [<font color=Green> Robotic </font>](#font-colorgreen-robotic-font-)
<!-- TOC -->

**---------------------------------目录-----------------------------**

## Deep Learning

### PETL: parameters effective transfer learning

> 相关链接：
> - NLP领域的Prompt Tuning综述：[链接](https://mp.weixin.qq.com/s/dz6Ad_pVveXwe6O0RvF7iw) 
> - [MAM adapter](https://mp.weixin.qq.com/s/dz6Ad_pVveXwe6O0RvF7iw): 对adapter等petl的相关变体进行了分析总结(推荐)
> - 常见的petl变体：[AIM](https://github.com/taoyang1122/adapt-image-models)(代码友好) ，[lora](https://arxiv.org/pdf/2106.09685.pdf)，[Adapter](http://proceedings.mlr.press/v97/houlsby19a/houlsby19a.pdf) ，[LST](https://github.com/ylsung/Ladder-Side-Tuning)
> - [知乎](https://zhuanlan.zhihu.com/p/635686756)上对的petl总结（强推）
> - 我自己的一些简单理解[petl简述](https://docs.google.com/presentation/d/14NLwCCgrwxSN30pNhAH5jUxKyRWuKS2r/edit?usp=drive_link)
>> ![aim-adapter.png](Images%2Faim-adapter.png), ![lst-adapter.png](Images%2Flst-adapter.png), ![mam-adapter.png](Images%2Fmam-adapter.png)

&nbsp;
### MTL，multi-task learning
> 一些参考链接
> - [知乎](https://www.zhihu.com/question/375794498)上关于多任务学习的回答
> - [多目标优化](https://proceedings.neurips.cc/paper_files/paper/2018/file/432aca3a1e345e339f35a30c8f65edce-Paper.pdf)经典论文
>

&nbsp;
### MoE, Mixture of Experts
> 一些参考链接：
> - [一文弄懂Mixture of Experts (MoE)的前世今生](https://mp.weixin.qq.com/s/u7bqG3skzklqDWu3MMmkzg)

&nbsp;
## NLP
&nbsp;


&nbsp;
## CV
&nbsp;

### <font color=Green> Facial expression recognition</font>
&nbsp;
> Siamese Masked Autoencoders (NeurIPS 2023 Oral)  
> [Paper](https://siam-mae-video.github.io/resources/paper.pdf), 
> [Code](https://siam-mae-video.github.io/),
> [Slide](Slide/2023.10.20-SiamMAE-陈银.pptx)
> ![img.png](Images/img.png)
>> 描述

&nbsp;

### <font color=Green> Image + Video pretrain for downstream tasks</font>
&nbsp;
> EVT: BERT Pretraining of Video Transformers (CVPR 2022)
> ![image](https://github.com/ReadingPapers/Report/assets/56926538/36d9776b-43a1-4336-b2d9-c71a30b0e2ad)
>> 描述: 将 BERT-Style 预训练的方式扩展到了Video task, 将视频表征学习解耦成空间学习和时间学习，预测 target 仿照 bert 预测 visual tokens

&nbsp;
> OmniMAE: Single Model Masked Pretraining on Images and Videos (CVPR 2023)
> ![image](https://github.com/ReadingPapers/Report/assets/56926538/694379e1-da39-4d82-b6cd-4fd7f9494ad5)
>> 描述: 提出了统一的编码器解码器，一个模型可以接受图像或者视频的输入，使用 Image+Video 预训练可以使用极高的掩码率（iamge:90%, video:95%), 提升了下游任务的性能

&nbsp;
> ViC-MAE: Self-Supervised Representation Learning from Images and Video with Contrastive Masked Autoencoders 
> ![image](https://github.com/ReadingPapers/Report/assets/56926538/2aa9cfc7-6816-4c1b-9d3d-0696946edcd2)
>> 描述:  加入了对比学习，进一步提升了模型的表征能力，同时在 Image 和 video相关的 task上达到 sota 性能


## Multimodality
&nbsp;

> Align before Fuse: Vision and Language
Representation Learning with Momentum Distillation (NeurIPS 2021)  
> [Paper](https://arxiv.org/abs/2107.07651), 
> [Code](https://github.com/salesforce/ALBEF),
> [Blog](https://blog.salesforceairesearch.com/align-before-fuse/),
> [Slide](Slide/2023.10.20-SiamMAE-陈银.pptx)
> ![img.png](Images/albef.png)
>>  - In this paper, we introduce a contrastive loss to ALign the image and
text representations BEfore Fusing (ALBEF) them through cross-modal attention,
which enables more grounded vision and language representation learning. Unlike
most existing methods, our method does not require bounding box annotations nor
high-resolution images.
>> - To improve learning from noisy web data, we propose
momentum distillation, a self-training method which learns from pseudo-targets
produced by a momentum model. We provide a theoretical analysis of ALBEF from
a mutual information maximization perspective, showing that different training
tasks can be interpreted as different ways to generate views for an image-text
pair

&nbsp;


## Embodied AI
&nbsp;
### <font color=Green> Navigation </font> 
&nbsp;
#### Visual language navigation
[论文阅读：Frequency-enhanced Data Augmentation for Vision-and-Language Navigation](http://t.csdnimg.cn/RI1p2)

&nbsp;
### <font color=Green> Manipulate </font> 
&nbsp;

### <font color=Green> Robotic </font> 
&nbsp;
