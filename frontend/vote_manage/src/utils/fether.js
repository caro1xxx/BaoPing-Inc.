import { HOST } from "@/ENV";
export const fether = (path, method = "get", params = {}) => {
  if (method === "get") {
    fetch(`${HOST}${path}`)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
      });
  } else if (method === "post") {
    return fetch(`${HOST}${path}`, {
      method: "post",
      body: JSON.stringify(params),
      headers: { "Content-Type": "application/json" },
    })
      .then((res) => res.json())
      .then((data) => data);
  }
};
