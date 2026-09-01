import { Link, useNavigate } from "react-router-dom";

function Profile() {
  const navigate = useNavigate();

  return (
    <div
      style={{
        display: "flex",
        minHeight: "100vh",
        fontFamily: "Arial, sans-serif",
        background: "#f4f6f9",
      }}
    >
      {/* Sidebar */}
      <div
        style={{
          width: "250px",
          background: "#1e293b",
          color: "white",
          padding: "25px",
        }}
      >
        <h2 style={{ marginBottom: "40px" }}>Insight Generation</h2>

        <div style={{ display: "flex", flexDirection: "column", gap: "20px" }}>
          <Link
            to="/dashboard"
            style={{ color: "white", textDecoration: "none" }}
          >
            🏠 Dashboard
          </Link>

          <Link
            to="/profile"
            style={{ color: "#38bdf8", textDecoration: "none", fontWeight: "bold" }}
          >
            👤 Profile
          </Link>

          <Link
            to="/settings"
            style={{ color: "white", textDecoration: "none" }}
          >
            ⚙ Settings
          </Link>

          <button
            onClick={() => navigate("/")}
            style={{
              marginTop: "30px",
              padding: "12px",
              border: "none",
              borderRadius: "8px",
              background: "#dc2626",
              color: "white",
              cursor: "pointer",
            }}
          >
            Logout
          </button>
        </div>
      </div>

      {/* Main */}
      <div style={{ flex: 1 }}>
        {/* Navbar */}
        <div
          style={{
            background: "white",
            padding: "20px 40px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
          }}
        >
          <h2>Profile</h2>

          <div style={{ display: "flex", gap: "20px" }}>
            <span style={{ fontSize: "24px" }}>🔔</span>
            <span style={{ fontSize: "24px" }}>👤</span>
          </div>
        </div>

        <div style={{ padding: "40px" }}>
          <div
            style={{
              background: "white",
              padding: "40px",
              borderRadius: "12px",
              boxShadow: "0 3px 10px rgba(0,0,0,0.08)",
            }}
          >
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: "30px",
              }}
            >
              <div
                style={{
                  width: "120px",
                  height: "120px",
                  borderRadius: "50%",
                  background: "#ddd",
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  fontSize: "50px",
                }}
              >
                👤
              </div>

              <div>
                <h1>insight_generation</h1>

                <p style={{ color: "#666" }}>
                 Tech | Instagram Analytics
                </p>

                <p style={{ marginTop: "15px" }}>
                  Helping creators understand their Instagram
                  performance using AI-driven analytics.
                </p>
              </div>
            </div>

            <hr style={{ margin: "30px 0" }} />

            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(4,1fr)",
                gap: "20px",
              }}
            >
              <div>
                <h3>Followers</h3>
                <h2>15,248</h2>
              </div>

              <div>
                <h3>Following</h3>
                <h2>432</h2>
              </div>

              <div>
                <h3>Posts</h3>
                <h2>86</h2>
              </div>

              <div>
                <h3>Account</h3>
                <h2>Business</h2>
              </div>
            </div>

            <hr style={{ margin: "30px 0" }} />

            <h2>Account Information</h2>

            <p>
              <strong>Email:</strong> demo@gmail.com
            </p>

            <p>
              <strong>Category:</strong> Technology
            </p>

            <p>
              <strong>Joined:</strong> January 2026
            </p>

            <p>
              <strong>Status:</strong> Connected ✅
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Profile;