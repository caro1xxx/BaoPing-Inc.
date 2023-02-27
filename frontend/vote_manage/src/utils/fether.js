import { HOST } from "@/ENV";
import isOnline from "is-online";
export const fether = async (path, method = "get", params = {}) => {
  let online = await isOnline();
  if (!online) {
    return "网络错误";
  }
  if (method === "get") {
    return fetch(`${HOST}${path}`)
      .then((res) => res.json())
      .then((data) => data);
  } else {
    return fetch(`${HOST}${path}`, {
      method: method,
      body: JSON.stringify(params),
      headers: { "Content-Type": "application/json" },
    })
      .then((res) => res.json())
      .then((data) => data);
  }
};
