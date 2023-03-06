import "./App.css";
import { LoadingOutlined } from "@ant-design/icons";
import { useEffect } from "react";
import { HOST } from "./ENV";
function App() {
  useEffect(() => {
    if (!window.location.search) return;
    fetch(
      `${HOST}/domain/getdomain?vote_id=${window.location.search.split("=")[1]}`
    )
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        if (!data.domain) return;
        window.location.href = `http://${data.domain}?vote_id=${
          window.location.search.split("=")[1]
        }`;
      });
  });

  return (
    <div className="Body">
      <LoadingOutlined
        style={{
          fontSize: 24,
          alignSelf: "center",
        }}
        spin
      />
    </div>
  );
}

export default App;
