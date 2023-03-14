import "./App.css";
import { useEffect, useState } from "react";
import useSWR from "swr";
import { HOST, CallBackUrl } from "./ENV";

function App() {
  const [baseInfo, setBaseInfo] = useState({
    appId: "wx14da5019fd445972",
    // redirectUri: "http://pay.yilsfeng.cn",
    redirectUri: HOST,
    // scope: "snsapi_base", // 授权方式
    scope: "snsapi_userinfo", // 授权方式
    code: "调用支付中...",
    msg: "",
  });

  // // 获取code
  // const getCode = () => {
  //   const url = `https://open.weixin.qq.com/connect/oauth2/authorize?appid=${
  //     baseInfo.appId
  //   }&redirect_uri=${encodeURIComponent(
  //     baseInfo.redirectUri
  //   )}&response_type=code&scope=${baseInfo.scope}&state=STATE#wechat_redirect`;
  //   window.location.href = url;
  //   refreshMsg(url);
  // };

  // 获取openid
  // const getOpen = () => {
  //   fetch(
  //     `http://pay.yilsfeng.cn/wechat/auth?code=${
  //       window.location.href.split("=")[1]
  //     }`
  //   )
  //     .then((res) => res.json())
  //     .then((data) => {
  //       refreshMsg(JSON.stringify(data));
  //     });
  // };

  const getParmas = () => {
    const q = {};
    window.location.search.replace(
      /([^?&=]+)=([^&]+)/g,
      (_, k, v) => (q[k] = v)
    );
    return q;
  };

  // 查询支付状态
  const queryPayState = () => {
    let url = `${HOST}/query/querypaymentstatus/?order_id=${getParmas().order}`;
    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        if (data.code === 200) {
          refreshMsg("支付成功 2秒后返回首页");
          setTimeout(() => {
            window.location.href =
              CallBackUrl +
              `?order_id=${getParmas().order}&openid=${
                getParmas().openid
              }&vote_id=${getParmas().vote_id}`;
          }, 2000);
        } else {
          refreshMsg("支付失败");
        }
      });
  };

  // 调用支付
  const getPay = () => {
    if (!getParmas().order) return;
    let url = `${HOST}/wechat/pay?order=${getParmas().order}`;
    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        if (!data) {
          refreshMsg("调用支付失败");
          return;
        }
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
              setTimeout(() => {
                queryPayState();
              }, 2000);
            } else {
              refreshMsg("支付被取消");
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

  useEffect(() => {
    getPay();
  }, []);

  const fetcher = (...args) =>
    fetch(...args).then((res) => {
      return res.json();
    });

  const { data, error, isLoading } = useSWR(
    `/wechat/queryOrder?order_id=${
      window.location.href.split("?")[1].split("=")[1]
    }`,
    fetcher
  );

  if (error) return <div>订单错误</div>;
  if (isLoading) return <div>loading...</div>;
  if (data.code !== 200) return <div>{data.msg}</div>;

  return (
    <div className="App">
      <div className="top"></div>
      <div className="body">
        <div>
          <svg
            t="1678761051718"
            className="prize_img"
            viewBox="0 0 1132 1024"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            p-id="2985"
            width="130"
            height="130"
          >
            <path
              d="M17.885047 226.624992h1096.949544c9.836776 0 17.885047 8.048271 17.885047 17.885047v213.428226c0 9.836776-8.048271 17.885047-17.885047 17.885047H17.885047c-9.836776 0-17.885047-8.048271-17.885047-17.885047V244.510039c0-9.836776 8.048271-17.885047 17.885047-17.885047z"
              fill="#FF505D"
              p-id="2986"
            ></path>
            <path
              d="M142.335165 475.823312h848.049308c6.557851 0 11.923365 5.365514 11.923365 11.923365V1012.076635c0 6.557851-5.365514 11.923365-11.923365 11.923365h-848.049308c-6.557851 0-11.923365-5.365514-11.923365-11.923365V487.746677c0-6.557851 5.365514-11.923365 11.923365-11.923365z"
              fill="#FF6174"
              p-id="2987"
            ></path>
            <path
              d="M258.438928 160.59936S128.474254 135.560294 102.540936 126.617771l45.904953 66.025631L65.578505 225.581697s193.903717 35.919136 402.860682 4.918388L367.835798 184.893215l-109.39687-24.293855zM351.888298 3.359989c-66.025632-11.774323-97.473506 11.178154-97.473506 11.178155l-18.034089 114.017174s46.650164-31.745958 101.944768-18.034089c71.987314 18.034089 162.008717 119.978856 162.008717 119.978856v-77.948996S441.313533 19.307489 351.888298 3.359989zM989.639263 192.643402l46.053996-66.025631c-25.933318 8.942523-155.897992 33.981589-155.897993 33.981589L770.398396 184.893215l-100.603389 45.755912c208.956965 31.000748 402.860682-5.06743 402.860682-5.06743L989.639263 192.643402zM901.704449 128.555318L883.819402 14.687186s-31.447874-22.952477-97.473506-11.178155C696.920662 19.456531 637.900007 152.700131 637.900007 152.700131v77.948996s89.872361-101.944767 161.859674-119.978856c55.145561-13.860911 101.944767 17.885047 101.944768 17.885047z"
              fill="#FFCA3E"
              p-id="2988"
            ></path>
            <path
              d="M491.83879 141.521977h149.042058V1024H491.83879z"
              fill="#FFCA3E"
              p-id="2989"
            ></path>
            <path
              d="M491.83879 479.99649h149.042058v544.00351H491.83879z"
              fill="#FFB82C"
              p-id="2990"
            ></path>
            <path
              d="M387.211266 127.959149c-64.982337-37.558599-142.186123-24.890024-150.681521 0.745211-9.38965 28.168949 36.664346 58.126402 103.286146 93.002244 43.818365 22.952477 160.667338 8.942523 160.667339 8.942523s-48.289627-65.280421-113.271964-102.689978zM901.704449 128.555318c-8.495397-25.635234-85.699183-38.303809-150.681521-0.745211s-113.271964 102.689978-113.271963 102.689978 116.998015 14.009953 160.667338-8.942523c66.6218-34.726799 112.675796-64.833295 103.286146-93.002244z"
              fill="#FFB82C"
              p-id="2991"
            ></path>
          </svg>
        </div>
        <div className="prize_name">
          <div className="text">
            {" "}
            {JSON.parse(data.data)[0].fields.prize_type}
          </div>
          <div className="przie_value">
            <svg
              t="1678761342290"
              class="icon"
              viewBox="0 0 1024 1024"
              version="1.1"
              xmlns="http://www.w3.org/2000/svg"
              p-id="5051"
              width="20"
              height="20"
            >
              <path
                d="M832.9 694.3c-115.2 172.3-286 266.5-410.5 236.1-0.2 0.2-0.5 0-0.7 0C311.5 916.7 192 801.8 129.1 636.5 51 430.7 90.8 225 217.5 177c82.2-31.3 180.9 11.6 261.7 101.7 124.3-118 273.4-161.9 370.8-97.1 124.3 83.1 116.6 312.7-17.1 512.7z"
                fill="#E50012"
                p-id="5052"
              ></path>
              <path
                d="M471.2 960.2c-17.9 0-35.4-1.9-52.3-5.8-0.3 0-0.7-0.1-1-0.1C296.1 938.7 171 814.5 106.5 645.1 67.3 541.4 55.3 434.2 72.9 343c18.4-95.3 66.7-162.3 136.1-188.5 83.9-32 184.1 1.8 271.5 90.4 131.8-115.8 283.4-149.5 382.9-83.3C998.6 252 993.9 497 853 707.7 748.9 863.3 599.1 960.2 471.2 960.2z m-47.9-53.8c1.6 0 3.2 0.3 4.7 0.7 116.4 28.4 278.2-66.7 384.8-226.1C939 492.2 949.6 277.2 836.6 201.6c-84.9-56.5-221.8-18.5-340.8 94.6-4.7 4.5-11 7.1-17.6 6.6-6.5-0.3-12.6-3.2-17-8-77.3-86.3-165.2-121.9-235.1-95.2-53.2 20.1-90.9 74.3-105.9 152.6-15.9 82.5-4.7 180.4 31.5 275.8 57.2 150.5 168.7 264.7 271.6 278.4z m409.6-212.1h0.2-0.2z"
                fill="#E50012"
                p-id="5053"
              ></path>
              <path
                d="M419.6 723.7c-3.5 0-7-0.8-10.3-2.3-12-5.7-17.1-20-11.5-32 1-2.2 25.9-53.9 77.1-67.5 32-8.5 65.9-0.5 100.6 23.8 0.7 0 4.7-1.6 6.9-5.2 19-31.2 56.6-92.4 117.6-85.6 13.2 1.5 22.7 13.4 21.3 26.6-1.5 13.2-13.6 22.6-26.6 21.3-30.7-3.7-56.3 38.5-70 61-9.5 15.5-23.6 25.6-39 28.8-13.5 2.8-26.9 0.2-37.8-7.5-22.3-15.7-42.6-21.4-60.3-16.8-29.5 7.7-46 41.3-46.2 41.6-4.2 8.8-12.8 13.8-21.8 13.8z"
                fill="#FFFFFF"
                p-id="5054"
              ></path>
            </svg>
            <div style={{ margin: "0px 10px" }}>
              {JSON.parse(data.data)[0].fields.price}元
            </div>
          </div>
          <div className="przie_value" style={{ marginTop: "20px" }}>
            <svg
              t="1678761640944"
              className="icon"
              viewBox="0 0 1024 1024"
              version="1.1"
              xmlns="http://www.w3.org/2000/svg"
              p-id="6235"
              width="20"
              height="20"
            >
              <path
                d="M512 64C264.57 64 64 264.58 64 512s200.57 448 448 448c247.42 0 448-200.58 448-448-0.34-247.28-200.72-447.66-448-448z m0 803.31c-196.24 0-355.31-159.08-355.31-355.31S315.76 156.69 512 156.69c196.23 0 355.31 159.08 355.31 355.31-0.34 196.09-159.22 354.97-355.31 355.31z"
                p-id="6236"
                fill="#cecece"
              ></path>
              <path
                d="M512 295.72h-92.69v308.97h308.97V512H512z"
                p-id="6237"
                fill="#cecece"
              ></path>
            </svg>
            <div>预计5分钟到账</div>
            <svg
              style={{ marginLeft: "10px" }}
              t="1678761712965"
              class="icon"
              viewBox="0 0 1024 1024"
              version="1.1"
              xmlns="http://www.w3.org/2000/svg"
              p-id="8815"
              width="20"
              height="20"
            >
              <path
                d="M575.12 131l94.74 192a47.68 47.68 0 0 0 35.9 26.08l211.84 30.78c39.11 5.68 54.72 53.74 26.43 81.33l-153.3 149.39a47.68 47.68 0 0 0-13.73 42.2l36.19 211c6.68 39-34.2 68.65-69.18 50.26l-189.46-99.62a47.68 47.68 0 0 0-44.38 0L320.7 914c-35 18.39-75.86-11.31-69.18-50.26l36.19-211A47.68 47.68 0 0 0 274 610.58L120.7 461.16c-28.3-27.58-12.68-75.65 26.43-81.33L359 349.05A47.68 47.68 0 0 0 394.87 323l94.73-192c17.49-35.43 68.03-35.43 85.52 0z"
                fill="#FED547"
                p-id="8816"
              ></path>
              <path
                d="M943.3 461.77c28.3-27.58 12.68-75.65-26.43-81.33L705 349.66a47.68 47.68 0 0 1-35.9-26.08l-94.74-192c-16.31-33.05-61.35-35.25-81.53-6.65a49.51 49.51 0 0 1 4 6.65l94.74 192a47.68 47.68 0 0 0 35.9 26.08l211.84 30.78c39.11 5.68 54.72 53.74 26.43 81.33L712.47 611.19a47.68 47.68 0 0 0-13.71 42.2l36.19 211a46.76 46.76 0 0 1-11.52 39.81l19.89 10.46c35 18.39 75.86-11.31 69.18-50.26l-36.19-211A47.68 47.68 0 0 1 790 611.19z"
                fill="#E2B742"
                p-id="8817"
              ></path>
              <path
                d="M263.93 925.77a54 54 0 0 1-53.06-63.05l36.19-211A41.47 41.47 0 0 0 235.13 615L81.85 465.6a53.88 53.88 0 0 1 29.87-91.9l211.83-30.78a41.51 41.51 0 0 0 31.23-22.69l94.73-192a53.89 53.89 0 0 1 96.64 0l94.74 192a41.5 41.5 0 0 0 31.23 22.69L884 373.7a53.88 53.88 0 0 1 29.86 91.9L760.53 615a41.45 41.45 0 0 0-11.93 36.71l36.19 211a53.88 53.88 0 0 1-78.18 56.8l-189.48-99.6a41.49 41.49 0 0 0-38.6 0l-189.47 99.61a53.86 53.86 0 0 1-25.13 6.25z m233.9-815.13a40.71 40.71 0 0 0-37.19 23.12l-94.73 192a53.89 53.89 0 0 1-40.57 29.47L113.5 386a41.48 41.48 0 0 0-23 70.75l153.3 149.39a53.88 53.88 0 0 1 15.5 47.69l-36.19 211a41.48 41.48 0 0 0 60.18 43.73l189.48-99.61a53.81 53.81 0 0 1 50.15 0l189.47 99.61a41.48 41.48 0 0 0 60.18-43.73l-36.19-211a53.86 53.86 0 0 1 15.5-47.69l153.28-149.42a41.48 41.48 0 0 0-23-70.75l-211.82-30.78a53.88 53.88 0 0 1-40.57-29.47L535 133.75a40.71 40.71 0 0 0-37.17-23.12z"
                fill="#28CA67"
                p-id="8818"
              ></path>
            </svg>
            <div style={{ fontWeight: "bold" }}> 4.8</div>
          </div>
          <div className="przie_value">
            <div style={{ textAlign: "start", width: "80%", color: "#000" }}>
              <div style={{ display: "flex", marginTop: "10px" }}>
                <div style={{ width: "50%" }}>礼物类型:</div>
                <div style={{ width: "50%", textAlign: "end" }}>
                  {JSON.parse(data.data)[0].fields.prize_type}
                </div>
              </div>
              <div style={{ display: "flex", marginTop: "10px" }}>
                <div style={{ width: "50%" }}>创建订单时间:</div>
                <div style={{ width: "50%", textAlign: "end" }}>
                  {JSON.parse(data.data)[0].fields.create_time}
                </div>
              </div>
              <div style={{ display: "flex", marginTop: "10px" }}>
                <div style={{ width: "50%" }}>订单号:</div>
                <div style={{ width: "50%", textAlign: "end" }}>
                  {JSON.parse(data.data)[0].fields.payment_order_id}
                </div>
              </div>
            </div>
          </div>
          <div className="przie_value">
            <div
              style={{
                marginTop: "20px",
                padding: "20px 20px",
                textAlign: "start",
                fontSize: "10px",
              }}
            >
              &nbsp;&nbsp;送出一份礼物为你喜欢的企业或选手加油打气,礼物虽少,心意但到
              <div>
                感谢您一直以来的信任和支持！我们致力于为您提供最好的产品和服务，让您的消费变得更加有价值和愉悦
              </div>
              我们的产品经过严格的质量控制和精心的设计，确保每一个细节都符合您的需求和期望
            </div>
          </div>
          <div className="przie_value" style={{ margin: "50px 0px" }}>
            {baseInfo.msg === "" ? <div className="loading"></div> : null}
          </div>
          <div className="fail">{baseInfo.msg}</div>
        </div>
      </div>
      {/* <button onClick={getCode}>获取code</button> */}
      {/* <button onClick={getOpen}>获取openid</button> */}
    </div>
  );
}
export default App;
