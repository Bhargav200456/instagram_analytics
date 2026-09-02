import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";

function Dashboard() {
  const navigate = useNavigate();

  const [keyword, setKeyword] = useState("Argentina Jersey");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeKeyword = async () => {
    if (!keyword.trim()) {
      setError("Please enter a product or topic.");
      return;
    }

    setLoading(true);
    setError("");
    setData(null);

    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/insights/search?keyword=${encodeURIComponent(
          keyword.trim()
        )}&clusters=3`
      );

      const result = await response.json();

      if (!response.ok || !result.success) {
        throw new Error(
          result.message || "Failed to analyze keyword."
        );
      }

      setData(result);
    } catch (err) {
      setError(
        err.message ||
          "Unable to connect to the backend. Make sure Flask is running."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        display: "flex",
        minHeight: "100vh",
        fontFamily: "Arial, sans-serif",
        background: "#f4f6f9",
      }}
    >
      {/* ================= SIDEBAR ================= */}

      <div
        style={{
          width: "230px",
          background: "#1e293b",
          color: "white",
          padding: "25px",
          flexShrink: 0,
        }}
      >
        <h2 style={{ marginBottom: "40px" }}>
          Insight Generation
        </h2>

        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "22px",
          }}
        >
          <Link
            to="/dashboard"
            style={{
              color: "white",
              textDecoration: "none",
              fontSize: "16px",
            }}
          >
            Dashboard
          </Link>

          <Link
            to="/clusters"
            style={{
              color: "white",
              textDecoration: "none",
              fontSize: "16px",
            }}
          >
            Clusters
          </Link>

          <Link
            to="/profile"
            style={{
              color: "white",
              textDecoration: "none",
              fontSize: "16px",
            }}
          >
            Profile
          </Link>

          <Link
            to="/settings"
            style={{
              color: "white",
              textDecoration: "none",
              fontSize: "16px",
            }}
          >
            Settings
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
              fontSize: "15px",
            }}
          >
            Logout
          </button>
        </div>
      </div>

      {/* ================= MAIN CONTENT ================= */}

      <div style={{ flex: 1 }}>
        {/* ================= NAVBAR ================= */}

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
          <h2 style={{ margin: 0 }}>
            Dashboard
          </h2>

          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: "20px",
            }}
          >
            <span
              style={{
                fontSize: "15px",
                color: "#666",
              }}
            >
              Instagram Insights
            </span>

            <div
              style={{
                width: "38px",
                height: "38px",
                borderRadius: "50%",
                background: "#2563eb",
                color: "white",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontWeight: "bold",
              }}
            >
              IG
            </div>
          </div>
        </div>

        {/* ================= DASHBOARD BODY ================= */}

        <div style={{ padding: "40px" }}>
          <h1 style={{ marginBottom: "8px" }}>
            Welcome Back
          </h1>

          <p
            style={{
              color: "#666",
              marginBottom: "30px",
            }}
          >
            Search Instagram topics and products, discover
            content clusters and generate AI-powered insights.
          </p>

          {/* ================= KEYWORD SEARCH ================= */}

          <div
            style={{
              background: "white",
              padding: "25px",
              borderRadius: "12px",
              boxShadow: "0 3px 10px rgba(0,0,0,0.08)",
              marginBottom: "30px",
            }}
          >
            <h2 style={{ marginTop: 0 }}>
              Analyze Product / Topic
            </h2>

            <p style={{ color: "#666" }}>
              Enter a product or topic to discover relevant
              public Instagram posts and generate AI insights.
            </p>

            <div
              style={{
                display: "flex",
                gap: "12px",
                marginTop: "20px",
                maxWidth: "750px",
              }}
            >
              <input
                type="text"
                value={keyword}
                onChange={(e) =>
                  setKeyword(e.target.value)
                }
                onKeyDown={(e) => {
                  if (e.key === "Enter") {
                    analyzeKeyword();
                  }
                }}
                placeholder="e.g. Argentina Jersey, Nike Shoes, Messi Jersey"
                style={{
                  flex: 1,
                  padding: "14px",
                  border: "1px solid #d1d5db",
                  borderRadius: "8px",
                  fontSize: "16px",
                  outline: "none",
                }}
              />

              <button
                onClick={analyzeKeyword}
                disabled={loading}
                style={{
                  padding: "14px 24px",
                  border: "none",
                  borderRadius: "8px",
                  background: loading
                    ? "#94a3b8"
                    : "#2563eb",
                  color: "white",
                  cursor: loading
                    ? "not-allowed"
                    : "pointer",
                  fontSize: "16px",
                  fontWeight: "bold",
                }}
              >
                {loading
                  ? "Analyzing..."
                  : "Analyze"}
              </button>
            </div>

            {loading && (
              <p
                style={{
                  marginTop: "15px",
                  color: "#2563eb",
                }}
              >
                Searching Instagram, collecting posts,
                creating clusters and generating AI insights.
                This may take a little while...
              </p>
            )}

            {error && (
              <div
                style={{
                  marginTop: "15px",
                  padding: "12px",
                  borderRadius: "8px",
                  background: "#fee2e2",
                  color: "#991b1b",
                }}
              >
                {error}
              </div>
            )}
          </div>

          {/* ================= STATS ================= */}

          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(3, 1fr)",
              gap: "20px",
              marginBottom: "40px",
            }}
          >
            {[
              [
                "Posts Analyzed",
                data ? data.total_posts : "--",
              ],
              [
                "Clusters Found",
                data ? data.total_clusters : "--",
              ],
              [
                "Search Topic",
                data ? data.keyword : "--",
              ],
            ].map(([title, value]) => (
              <div
                key={title}
                style={{
                  background: "white",
                  padding: "25px",
                  borderRadius: "12px",
                  boxShadow:
                    "0 3px 10px rgba(0,0,0,0.08)",
                }}
              >
                <p
                  style={{
                    margin: 0,
                    color: "#666",
                    fontSize: "14px",
                  }}
                >
                  {title}
                </p>

                <h2
                  style={{
                    marginTop: "10px",
                    marginBottom: 0,
                    color: "#1e293b",
                    wordBreak: "break-word",
                  }}
                >
                  {value}
                </h2>
              </div>
            ))}
          </div>

          {/* ================= RESULTS ================= */}

          {data && data.clusters && (
            <div>
              <h2 style={{ marginBottom: "20px" }}>
                AI Generated Cluster Insights
              </h2>

              <div
                style={{
                  display: "grid",
                  gridTemplateColumns:
                    "repeat(2, 1fr)",
                  gap: "25px",
                }}
              >
                {data.clusters.map((cluster) => (
                  <div
                    key={cluster.cluster_id}
                    style={{
                      background: "white",
                      borderRadius: "12px",
                      padding: "25px",
                      boxShadow:
                        "0 3px 10px rgba(0,0,0,0.08)",
                    }}
                  >
                    {/* Cluster heading */}

                    <div
                      style={{
                        display: "flex",
                        justifyContent:
                          "space-between",
                        alignItems: "center",
                        marginBottom: "15px",
                        gap: "10px",
                      }}
                    >
                      <h2
                        style={{
                          margin: 0,
                          color: "#1e293b",
                        }}
                      >
                        {cluster.cluster_name}
                      </h2>

                      <span
                        style={{
                          background: "#dbeafe",
                          color: "#1d4ed8",
                          padding: "6px 10px",
                          borderRadius: "20px",
                          fontSize: "13px",
                          fontWeight: "bold",
                          whiteSpace: "nowrap",
                        }}
                      >
                        {cluster.post_count} posts
                      </span>
                    </div>

                    {/* AI Insight */}

                    <div
                      style={{
                        background: "#f8fafc",
                        borderLeft:
                          "4px solid #2563eb",
                        padding: "15px",
                        borderRadius: "6px",
                        marginBottom: "20px",
                      }}
                    >
                      <h4
                        style={{
                          marginTop: 0,
                          marginBottom: "8px",
                        }}
                      >
                        AI Insight
                      </h4>

                      <p
                        style={{
                          margin: 0,
                          color: "#475569",
                          lineHeight: "1.6",
                        }}
                      >
                        {cluster.insight}
                      </p>
                    </div>

                    {/* Posts */}

                    <h4>
                      Posts in this cluster
                    </h4>

                    <div
                      style={{
                        display: "flex",
                        flexDirection:
                          "column",
                        gap: "15px",
                      }}
                    >
                      {cluster.posts &&
                        cluster.posts.map(
                          (post, index) => (
                            <div
                              key={
                                post.id ||
                                post.post_url ||
                                index
                              }
                              style={{
                                display: "flex",
                                gap: "15px",
                                borderTop:
                                  "1px solid #e5e7eb",
                                paddingTop: "15px",
                              }}
                            >
                              {post.image_url && (
                                <img
                                  src={
                                    post.image_url
                                  }
                                  alt="Instagram post"
                                  style={{
                                    width: "80px",
                                    height: "80px",
                                    objectFit:
                                      "cover",
                                    borderRadius:
                                      "8px",
                                  }}
                                />
                              )}

                              <div
                                style={{
                                  flex: 1,
                                }}
                              >
                                <p
                                  style={{
                                    margin:
                                      "0 0 6px 0",
                                    color:
                                      "#374151",
                                    fontSize:
                                      "14px",
                                    lineHeight:
                                      "1.4",
                                  }}
                                >
                                  {post.caption
                                    ? post.caption
                                        .length >
                                      150
                                      ? post.caption.substring(
                                          0,
                                          150
                                        ) + "..."
                                      : post.caption
                                    : "No caption available"}
                                </p>

                                <span
                                  style={{
                                    fontSize:
                                      "12px",
                                    color:
                                      "#888",
                                  }}
                                >
                                  {post.content_type ||
                                    "Post"}
                                </span>

                                {post.post_url && (
                                  <div
                                    style={{
                                      marginTop:
                                        "8px",
                                    }}
                                  >
                                    <a
                                      href={
                                        post.post_url
                                      }
                                      target="_blank"
                                      rel="noreferrer"
                                      style={{
                                        fontSize:
                                          "12px",
                                        color:
                                          "#2563eb",
                                        textDecoration:
                                          "none",
                                      }}
                                    >
                                      View Instagram Post
                                    </a>
                                  </div>
                                )}
                              </div>
                            </div>
                          )
                        )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* ================= INITIAL STATE ================= */}

          {!data &&
            !loading &&
            !error && (
              <div
                style={{
                  background: "white",
                  padding: "50px",
                  borderRadius: "12px",
                  textAlign: "center",
                  boxShadow:
                    "0 3px 10px rgba(0,0,0,0.08)",
                }}
              >
                <h2>
                  Start Your Analysis
                </h2>

                <p style={{ color: "#666" }}>
                  Enter a product or topic above and
                  click <strong>Analyze</strong> to
                  discover Instagram content clusters
                  and generate AI-powered insights.
                </p>
              </div>
            )}
        </div>
      </div>
    </div>
  );
}

export default Dashboard;