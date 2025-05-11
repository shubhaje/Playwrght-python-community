# Test user credentials by environment
USER_CREDENTIALS = {
    "SIT": {
        "standard_user": {
            "username": "standard_user",
            "password": "secret_sauce"
        },
        "locked_out_user": {
            "username": "locked_out_user",
            "password": "secret_sauce"
        },
        "problem_user": {
            "username": "problem_user",
            "password": "secret_sauce"
        },
        "performance_glitch_user": {
            "username": "performance_glitch_user",
            "password": "secret_sauce"
        },
        "error_user": {
            "username": "error_user",
            "password": "secret_sauce"
        },
        "visual_user": {
            "username": "visual_user",
            "password": "secret_sauce"
        }
    },
    "UAT": {
        "standard_user": {
            "username": "uat_standard_user",
            "password": "uat_secret_sauce"
        },
        "locked_out_user": {
            "username": "uat_locked_out_user", 
            "password": "uat_secret_sauce"
        },
        "problem_user": {
            "username": "uat_problem_user",
            "password": "uat_secret_sauce"
        },
        "performance_glitch_user": {
            "username": "uat_performance_glitch_user",
            "password": "uat_secret_sauce"
        },
        "error_user": {
            "username": "uat_error_user",
            "password": "uat_secret_sauce"
        },
        "visual_user": {
            "username": "uat_visual_user",
            "password": "uat_secret_sauce"
        }
    }
}

# Default environment
DEFAULT_ENV = "SIT"