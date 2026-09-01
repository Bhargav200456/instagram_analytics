import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#f5f7fb",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        fontFamily: "Arial"
      }}
    >
      <div
        style={{
          width: "650px",
          background: "white",
          padding: "50px",
          borderRadius: "20px",
          textAlign: "center",
          boxShadow: "0 10px 30px rgba(0,0,0,0.1)"
        }}
      >
        <h1
          style={{
            fontSize: "50px",
            marginBottom: "20px"
          }}
        >
          Insight Generation
        </h1>

        <h2
          style={{
            color: "#666"
          }}
        >
          AI Powered Instagram Analytics Platform
        </h2>

        <p
          style={{
            marginTop: "20px",
            lineHeight: "30px",
            color: "#777"
          }}
        >
          Analyze your Instagram Business account,
          monitor engagement, track followers,
          and gain AI powered insights.
        </p>

        <button
          onClick={() => navigate("/dashboard")}
          style={{
            marginTop: "35px",
            padding: "16px 40px",
            border: "none",
            borderRadius: "10px",
            background: "#E1306C",
            color: "white",
            fontSize: "18px",
            cursor: "pointer"
          }}
        >
          Login with Instagram
        </button>
      </div>
    </div>
  );
}

export default Home;