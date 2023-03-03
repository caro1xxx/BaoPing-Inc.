import { HOST } from "@/ENV";
import isOnline from "is-online";
export const fether = async (
  path,
  method = "get",
  params = {},
  name = "",
  target = ""
) => {
  let online = await isOnline();
  if (!online) {
    return "网络错误";
  }
  if (method === "get") {
    return fetch(`${HOST}${path}`)
      .then((res) => res.json())
      .then((data) => data);
  } else {
    fetch(`${HOST}/logs/`, {
      method: "post",
      body: JSON.stringify({
        who: name,
        action:
          method === "post" ? "添加" : method === "delete" ? "删除" : "修改",
        target: target,
        token: params.token,
      }),
      headers: { "Content-Type": "application/json" },
    });
    return fetch(`${HOST}${path}`, {
      method: method,
      body: JSON.stringify(params),
      headers: { "Content-Type": "application/json" },
    })
      .then((res) => res.json())
      .then((data) => data);
  }
};
