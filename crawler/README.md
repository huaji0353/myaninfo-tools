# 基于mongodb的动画番剧信息数据库

## 系统设计
#### 前端
dj or flask 直接渲染view 可视化同理

#### 后端
1. scrapy.Item单文档（储存string）

2. mongodb(db.document)+ORM（读取string并格式化）
 
# 数据格式定义手册

## 基础实现 x86(int32)
字符串 BaseString(document) 语言翻译
{
    中文 zh:String
    日语 jp:String
    英语 en:String
    罗马音 nhg:String
}

个体/实体 BaseIndiv(document) 用于集合与生物描述
{
    个体ID _id:ObjectId(int32)
    名称 name:BaseString()
    生日 birth:DateTime
    标签 label:Array[String]
}

生物个体/身份证 BaseIndivMan(BaseIndiv) 动画角色和现实人类描述
{
    个体ID _id:BaseIndiv._id
    名称 name:BaseIndiv.name
    生日 birth:BaseIndiv.birth
    标签 tags:BaseIndiv.tags
    性别 sex:Boolean
}

集合/构成 BaseCollect(BaseIndiv) 制作组/公司和动画制作集合
{
    集合ID _id:BaseIndiv._id
    名称 name:BaseIndiv.name
    创建日期 birth:BaseIndiv.birth
    标签 label:BaseIndiv.label
    成员 members:{String:{String:ObjectId}dict/document / String:Array[ObjectId]} 有序集合 无序集合
}

## 实例实现
参与人员 Staff(BaseIndivMan)
{

}

人物角色 Character(BaseIndivMan)
{

}

工作室/制作公司 Studio(BaseCollect)
{

}

动画/番剧 Anime(BaseCollect)
{
    名称 name:BaseCollect.name
    工作室 works:BaseCollect.members
    类型 genre:BaseCollect.label
    
}

{
    "name": "", 
    "cover": None,  # 封面(base64/blob/url)
    "time": [2000, 10],  # 放送开始(yy/mm)
    "episodes": {},  # 分集 エピソード
    "staff": {},  # 参与人员 スタッフ
    "baseinfos": {},  # 一些基本信息
    "story": "",  # 故事简介 ストーリー
    "character&cast": [], # 角色设定&演员 キャラクター&キャスト
    "tags":  # 标签
    {
        "genre": [""],  # 类型
        "label_bgmtv": {},  # bgmtv的标注数据
    },
    "ranking": {"bgmtv":8, } # 评分
    "cast": {},  # 角色
    "relate":  # 相关
    {
        "bgm": [],  # 音乐
        "series": [],  # 系列
        "recommend": [],  # 相关推荐
    },
    "origin": {},  # 引用来源请注名
    "streaming" : {}, # 国内授权流提供商 動画配信
}

## 需实现的结构（非描述或实体）
能够通过计算推导
关系

不能通过计算推导
动画构成

## 统计时权重分配
原作 + 设定 + 导演
原作 + 脚本 => 题材
分镜+演出+原画+摄影
: 脚本+故事 -观众-> 标签 tags
: 脚本/故事 story -观众-> genre 种类/类型