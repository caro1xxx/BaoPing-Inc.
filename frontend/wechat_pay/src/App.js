import "./App.css";
import { useState } from "react";

function App() {
  const [baseInfo, setBaseInfo] = useState({
    appId: "wx14da5019fd445972",
    redirectUri: "http://pay.yilsfeng.cn",
    // scope: "snsapi_base", // 授权方式
    scope: "snsapi_userinfo", // 授权方式
    code: 0,
    msg: "",
  });
  // 获取code
  const getCode = () => {
    const url = `https://open.weixin.qq.com/connect/oauth2/authorize?appid=${
      baseInfo.appId
    }&redirect_uri=${encodeURIComponent(
      baseInfo.redirectUri
    )}&response_type=code&scope=${baseInfo.scope}&state=STATE#wechat_redirect`;
    window.location.href = url;
    refreshMsg(url);
  };

  // 获取openid
  const getOpen = () => {
    fetch(
      `http://pay.yilsfeng.cn/wechat/auth?code=${
        window.location.href.split("=")[1]
      }`
    )
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        refreshMsg(JSON.stringify(data));
      });
  };
  // 调用支付
  const getPay = () => {
    let params = getParams();
    let url = `http://pay.yilsfeng.cn/wechat/pay?name=${params.name}&fee=${params.fee}&openid=${params.openid}&vote_id=${params.vote_id}`;
    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        refreshMsg(JSON.stringify(data));
        if (!data) return;
        /* eslint-disable */
        WeixinJSBridge.invoke(
          "getBrandWCPayRequest",
          {
            appId: "wx14da5019fd445972", //公众号ID，由商户传入
            timeStamp: data.timestamp + "", //时间戳，自1970年以来的秒数
            nonceStr: data.nonceStr, //随机串
            package: data.package,
            signType: "MD5", //微信签名方式：
            paySign: data.paySign, //微信签名
          },
          function (res) {
            if (res.err_msg == "get_brand_wcpay_request:ok") {
              refreshMsg("支付成功");
            }
          }
        );
      });
  };

  // 刷新页面提示
  const refreshMsg = (info) => {
    let newBaseInfo = { ...baseInfo };
    newBaseInfo.msg = info;
    setBaseInfo(newBaseInfo);
  };

  // 获取url参数
  const getParams = () => {
    const params = window.location.href.split("?")[1].split("&");
    console.log(params);
    return {
      name: params[0].split("=")[1],
      fee: params[1].split("=")[1],
      openid: params[2].split("=")[1],
      vote_id: params[3].split("=")[1],
    };
  };
  return (
    <div className="App">
      <div>{baseInfo.msg}</div>
      <div>
        <button onClick={getCode}>获取code</button>
      </div>
      <div>
        <button onClick={getOpen}>获取openid</button>
      </div>
      <div>
        <button onClick={getPay}>调用支付</button>
      </div>
      <div>
        <button onClick={getParams}>获取参数</button>
      </div>
    </div>
  );
}
export default App;
