import { HOST } from "@/ENV";
export const fether = (path, method = "get", params = {}) => {
  if (method === "get") {
    return fetch(`${HOST}${path}`)
      .then((res) => res.json())
      .then((data) => {
        if (data.code === 200) {
          return JSON.parse(data.data);
        } else {
          return false;
        }
      });
  } else {
    return fetch(HOST + path, {
      method: method,
      body: JSON.stringify(params),
      headers: { "Content-Type": "application/json" },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.code !== 200) {
          return false;
        } else {
          return JSON.parse(data.data);
        }
      });
  }
};
