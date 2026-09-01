import { useNavigate } from "react-router-dom";

function LoginButton() {

    const navigate = useNavigate();

    return (

        <button
            className="login-btn"
            onClick={() => navigate("/dashboard")}
        >
            Login with Instagram
        </button>

    );

}

export default LoginButton;