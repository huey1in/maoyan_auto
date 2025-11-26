#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time
import os
from urllib.parse import urlencode

class MaoyanAPI:
    """猫眼演出API客户端"""

    def __init__(self, config_file="config.json"):
        """
        初始化API客户端
        :param config_file: 配置文件路径
        """
        # 加载配置文件
        self.config = self._load_config(config_file)

        self.base_url = self.config["base_url"]
        self.session = requests.Session()

        # 从配置文件读取认证信息
        self.uuid = self.config["uuid"]
        self.token = self.config["token"]

        # 公共参数
        self.common_params = {
            "uuid": self.uuid,
            "cityId": self.config["cityId"],
            "clientPlatform": self.config["clientPlatform"],
            "sellChannel": self.config["sellChannel"],
            "optimus_risk_level": self.config["optimus_risk_level"],
            "optimus_code": self.config["optimus_code"],
            "ax": self.config["ax"],
            "bx": self.config["bx"],
            "yodaReady": self.config["yodaReady"],
            "csecplatform": self.config["csecplatform"],
            "csecversion": self.config["csecversion"]
        }

        # 通用请求头
        self.headers = {
            "Host": "yanchu.maoyan.com",
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-S908E Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/129.0.6668.70 Safari/537.36 TitansX/21.0.2.4-target30 KNB/1.2.0 android/9 maoyan/com.sankuai.movie/9.73.0 App/10420/9.73.0 Maoyan/9.73.0",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://h5.dianping.com",
            "Referer": "https://h5.dianping.com/",
            "X-Requested-With": "com.sankuai.movie",
            "sec-ch-ua-platform": '"Android"',
            "sec-ch-ua": '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        }

        # Cookies
        self.cookies = {
            "_utm_campaign": "AmovieBmovieCD-1",
            "_utm_source": "QQ",
            "_utm_medium": "android",
            "_utm_content": "7428fd5f1a09367394efde53e44289d7",
            "cityid": str(self.config["cityId"]),
            "uuid": self.uuid,
            "_utm_term": "9.73.0",
            "token": self.token
        }

    def _load_config(self, config_file):
        """加载配置文件"""
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"配置文件不存在: {config_file}")

        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)

        print(f"已加载配置文件: {config_file}")
        return config

    def _generate_mtgsig(self):
        """
        生成mtgsig签名
        从配置文件读取签名参数
        """
        return json.dumps(self.config["mtgsig"], separators=(',', ':'))

    def _request(self, method, url, params=None, data=None, need_token=False):
        """统一请求方法"""
        # 合并参数
        if params:
            full_params = {**self.common_params, **params}
        else:
            full_params = self.common_params.copy()

        # 如果需要token，添加到参数中
        if need_token:
            full_params["token"] = self.token

        # 添加mtgsig签名
        headers = self.headers.copy()
        headers["mtgsig"] = self._generate_mtgsig()

        # 发送请求
        try:
            if method.upper() == "GET":
                response = self.session.get(
                    url,
                    params=full_params,
                    headers=headers,
                    cookies=self.cookies,
                    timeout=10
                )
            elif method.upper() == "POST":
                headers["Content-Type"] = "application/json;charset=UTF-8"
                response = self.session.post(
                    url,
                    params=full_params,
                    json=data,
                    headers=headers,
                    cookies=self.cookies,
                    timeout=10
                )
            else:
                raise ValueError(f"不支持的请求方法: {method}")

            # 打印请求信息
            print(f"请求URL: {method.upper()} {response.url}")
            print(f"状态码: {response.status_code}")
            print(f"响应头:")
            for key, value in response.headers.items():
                if key in ['Token', 'ServerTime', 'M-TraceId']:
                    print(f"  {key}: {value}")

            # 返回响应
            return response

        except Exception as e:
            print(f"\n请求失败: {str(e)}")
            return None

    def get_project_detail(self, project_id=415604):
        """获取项目详情"""
        print(f"\n>>> 获取项目详情 (projectId={project_id})")
        url = f"{self.base_url}/my/odea/project/detail"
        params = {
            "projectId": project_id,
            "buyInstructionType": 1,
            "detailType": 1
        }
        response = self._request("GET", url, params=params, need_token=True)

        if response and response.status_code == 200:
            try:
                data = response.json()
                print(f"\n响应数据 (部分):")
                print(json.dumps(data, ensure_ascii=False, indent=2)[:500] + "...")
                return data
            except Exception as e:
                print(f"解析响应失败: {str(e)}")
        return None


def main():
    """主函数 - 测试各个接口"""
    print("猫眼演出API调试脚本")

    # 创建API客户端
    api = MaoyanAPI()

    # 从配置文件读取测试参数
    project_id = api.config["project_id"]

    # 1. 获取项目详情
    print(f"\n\n获取项目详情 (projectId={project_id})")
    detail = api.get_project_detail(project_id)

    print("测试完成!")

    # 总结
    print("\n总结:")
    print(f"项目详情接口: {'[OK] 成功' if detail else '[FAIL] 失败'}")

    if detail:
        print("\n接口调用成功")
    else:
        print("\n接口调用失败")


if __name__ == "__main__":
    main()
