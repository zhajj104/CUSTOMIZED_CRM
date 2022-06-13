# CUSTOMIZED_CRM
一、背景  
Odoo的CRM功能强大，将线索和商机作为CRM应用程序的一部分，使用销售漏斗组织这些商机，可以对商机按所处的阶段来进行分类管理。不过Odoo本身由国外开发，国内使用的时候难免有些不便，因此，本文将介绍一个自定义的CRM应用用来适配国内人员。
  
	
二、自定义CRM应用介绍  
自定义CRM应用一共包含客户、联系人、Pipeline和产品等四个模块，其中客户、联系人和产品为基础模块，Pipeline模块集中了主要功能点。  

1.客户模块  
客户模块列表页包含客户名称、客户类型、客户经理等信息，点击创建分别填入以下四类信息：基本信息、地区定位、工商信息和组织信息，其中客户名称字段为必填项。客户模块与Pipeline、联系人两个模块关联。  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/client.png)  
2.联系人模块  
联系人模块列表页包含姓名、客户名称、电话等信息，点击创建分别填入以下四类信息：基本信息、个人情况、个人情况、社会关系和工作情况，其中姓名、性别、部门、职务、手机电话和邮箱等字段为必填项，客户名称字段关联客户模块，即从客户列表中选取。  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/contact.png)  
3.Pipeline模块  
Pipeline模块列表页包含商机名称、负责人、商机流程、商机阶段、商机金额、代理商名称、预计签约日期和创建时间等信息，列表下方会显示当前页面的商机金额之和。  
商机阶段是一个Many2one的关联字段，关联crm_business_stage表，该表有商机出现、方案交流、投标及报价、中标及商务、赢单、输单、项目中止、落单、需求挖掘、项目立项、厂商中标、中标/准备签约、商务沟通、已经下单付款和预交付等预设值，可以酌情修改。  
商机流程设有项目分销、海量分销、客户直销和推荐关联四个预设值，可以酌情修改。  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/pipeline_1.png)  
点击创建填入两个tag页：“详细信息”和“商机明细”。在“详细信息”tag页分别填入以下五类信息：商机出现、方案及交流、招投标及报价、中标及商务和关单管理，其中商机名称字段为必填项。在“商机明细”tag页填入预设业务类型，点击“添加明细行”，即创建一个商机明细，包括基本信息和系统信息两部分内容。“商机明细”列表页是Pipeline关联的“crm.business.detail”商机明细表，其中“产品线名称”为Many2one字段，关联到即将介绍的“crm.products”产品模块。  
回到Pipeline列表页，发现多出一个“Pipeline作废”按钮，点击该按钮后，对应的Pipeline记录将不会出现在列表中。  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/pipeline_2.png)  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/pipeline_3.png)  
如果后续想恢复该条Pipeline记录，需要在自定义筛选里选择“Active为假”条件，应用后点击“恢复”按钮，此时需要清除“Active为假”的筛选条件，否则该条Pipeline记录也不会出现在列表中。  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/pipeline_4.png)  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/pipeline_5.png)  
进入该条Pipeline记录的详情页，页面内同样新增了一个“Pipeline作废”按钮，效果与列表页的按钮一样，此外还有商机阶段进度条，可以选择不同的商机阶段显示不同的效果。  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/pipeline_6.png)  
pipeline除了列表展示还可以通过右上角点击切换看板和日历两种展示方式。  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/pipeline_7.png)  
点击看板按钮，所有的pipeline信息将按照商机阶段进行分类，并且默认收拢3个看板。  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/pipeline_8.png)  
点击日历按钮，所有的pipeline信息将按照创建时间进行分类。点击条目可以进行编辑；点击空白处填写摘要点击创建按钮可以快速创建一条pipeline记录，也可以点击编辑按钮创建一条完整的pipeline记录。  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/pipeline_9.png)  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/pipeline_10.png)  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/pipeline_11.png)  
4.产品模块  
产品模块列表页包含产品名称、产品归属系统、分类和产品概述等信息，点击创建分别填入以下三类信息：基本信息、激励比例和系统信息。  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/product_1.png)  
点击保存之后详情页可以看到一个产品可以关联多个商机明细。  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/product_2.png)  
如图，我们在Pipeline模块的“商机1”记录中增加一条产品线名称为“产品1”的商机明细，那么在“产品1”的商机明细里对应也会自动加上这条商机明细记录。  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/product_3.png)  
![Image text](https://github.com/zhajj104/CUSTOMIZED_CRM/blob/13.0/customized_crm/img/product_4.png)  

三、结束语  
自定义CRM模块暂时就介绍到这里了，这只是初级阶段，还有“流程列表”、“线索转换记录”、“审批流程”和“修改记录”等逻辑需补充，后续也会新增更多功能。  
