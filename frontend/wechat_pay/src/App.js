import "./App.css";
import { useState } from "react";
function App() {
  const [baseInfo, setBaseInfo] = useState({
    appId: "wx0656a23d2fe51585",
    redirectUri: "http://pay.yilsfeng.cn/",
    scope: "snsapi_base",
    grant_type: "client_credential",
    code: 0,
    msg: "",
  });

  // code
  const getCode = () => {
    const url = `https://open.weixin.qq.com/connect/oauth2/authorize?appid=${
      baseInfo.appId
    }&redirect_uri=${encodeURIComponent(
      baseInfo.redirectUri
    )}&response_type=code&scope=${baseInfo.scope}&state=STATE#wechat_redirect`;
    window.location.href = url;
  };

  // // openid
  // const getOpen = () => {
  //   console.log(window.location.href.split("=")[1]);
  //   // fetch(
  //   //   `http://pay.yilsfeng.cn/user_info?code=${
  //   //     window.location.href.split("=")[1]
  //   //   }`
  //   // )
  //   //   .then((res) => res.json())
  //   //   .then((data) => {
  //   //     let newBaseInfo = { ...baseInfo };
  //   //     newBaseInfo.msg = JSON.stringify(data);
  //   //     setBaseInfo(newBaseInfo);
  //   //   });
  // };

  // access_token
  // const getAccessToken = () => {
  //   fetch(
  //     `https://api.weixin.qq.com/cgi-bin/token?grant_type=${baseInfo.grant_type}&appid=${baseInfo.appId}&secret=APPSECRET`
  //   );
  // };

  return (
    <div className="App">
      <div>{baseInfo.msg}</div>
      <div>
        <button onClick={getCode}>获取code</button>
      </div>
      {/* <button>支付</button> */}
    </div>
  );
}

export default App;
