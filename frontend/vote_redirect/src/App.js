import "./App.css";
import { LoadingOutlined } from "@ant-design/icons";
import { useEffect, useState } from "react";
import { HOST } from "./ENV";
function App() {
  const [domain, setDomain] = useState("");

  useEffect(() => {
    if (domain) return;
    fetch(`${HOST}/domain/getdomain`)
      .then((res) => res.json())
      .then((data) => {
        setDomain(data.domain);
        window.location.href = "https://" + data.domain;
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
