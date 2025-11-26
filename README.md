# 未完成
## 2025.11.26
## 抓包接口脚本请求响应数据结果
```bash
已加载配置文件: config.json


获取项目详情 (projectId=415604)

>>> 获取项目详情 (projectId=415604)
请求URL: GET https://yanchu.maoyan.com/my/odea/project/detail?uuid=00000000000001EA6BA9EA3D04C15AE85F065738E854BA175985095024794050&cityId=1&clientPlatform=1&sellChannel=5&optimus_risk_level=71&optimus_code=10&ax=187450533&bx=196395859&yodaReady=h5&csecplatform=4&csecversion=4.0.4&projectId=415604&buyInstructionType=1&detailType=1&token=AgHSJZ3-8_OI8Caem8FRhVrDgpYhK0mw1L1SoxFAuhIv2NbItuHyl6BCXG96EQ43ANRGlElf5dgLIwAAAACRLQAAYY2k7YgDsJat08Dc4KLUa_XbHQt13ZI2yiJpxGUWQUzSxsiITuUIx7H8ou7x1LjI
状态码: 200
响应头:
  M-TraceId: 5113909081036962408
  Token: AgHSJZ3-8_OI8Caem8FRhVrDgpYhK0mw1L1SoxFAuhIv2NbItuHyl6BCXG96EQ43ANRGlElf5dgLIwAAAACRLQAAYY2k7YgDsJat08Dc4KLUa_XbHQt13ZI2yiJpxGUWQUzSxsiITuUIx7H8ou7x1LjI
  ServerTime: 1764161858375

响应数据 (部分):
{
  "success": true,
  "data": {
    "baseProjectVO": {
      "performanceId": 415604,
      "categoryId": 1,
      "name": "【济南】李荣浩「黑马」世界巡回演唱会-济南站",
      "ticketStatus": 5,
      "unusualSaleStatus": 0,
      "saleStatus": 6,
      "buttonContext": {
        "code": 9,
        "message": "已结束"
      },
      "ticketNotes": "[{\"code\":7,\"content\":\"一人一票，儿童须购票并持有效证件入场\",\"order\":5,\"showInUserTerminal\":true,\"title\":\"儿童说明\",\"type\":1},{\"code\":8,\"content\":\"该项目支持开具电子发票，请在演出结束前通过订单详情页提...
```
## 暂时只抓包到了演唱会门票查询接口，可以知道演唱会通过字段performanceId区分，学业太忙有时间再研究吧
