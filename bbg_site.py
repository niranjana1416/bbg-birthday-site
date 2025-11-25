from flask import Flask, request
from flask import render_template_string

app = Flask(__name__)

# ----------------------------------------------
# HTML + CSS + JS stored inside Python variable
# ----------------------------------------------
main_page = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Are you my BBG?</title>

    <!-- handwritten fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Patrick+Hand&display=swap" rel="stylesheet">

    <style>
        body {
            background: linear-gradient(#ffe1ef, #ffb6d9);
            font-family: 'Patrick Hand', cursive;
            text-align: center;
            padding-top: 130px;
            color: #ff4f9a;
        }

        h1 {
            font-size: 42px;
        }

        button {
            font-size: 25px;
            padding: 12px 28px;
            border-radius: 15px;
            border: none;
            cursor: pointer;
            margin: 15px;
            font-family: 'Patrick Hand', cursive;
            background: white;
            color: #ff4f9a;
            box-shadow: 0 0 15px #ff8fca;
            transition: 0.3s;
        }

        button:hover {
            transform: scale(1.15);
            background: #ffd6e9;
        }

        /* Floating hearts */
        .heart {
            position: fixed;
            bottom: -50px;
            font-size: 24px;
            animation: floatUp 6s linear infinite;
            opacity: 0.8;
        }

        @keyframes floatUp {
            0% { transform: translateY(0) scale(1); opacity: 0.9; }
            100% { transform: translateY(-130vh) scale(1.7); opacity: 0; }
        }
    </style>
</head>

<body>

    <h1>Are you my BBG? 💗✨</h1>

    <form action="/answer">
        <button name="bbg" value="yes">Yes 😚💞</button>
        <button name="bbg" value="no">No 🙄</button>
    </form>

    <script>
        function createHeart() {
            const heart = document.createElement("div");
            heart.classList.add("heart");
            heart.innerHTML = Math.random() > 0.5 ? "💗" : "❤️";
            heart.style.left = Math.random() * 100 + "vw";
            heart.style.animationDuration = (4 + Math.random() * 3) + "s";
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 6000);
        }
        setInterval(createHeart, 450);
    </script>

</body>
</html>
"""

# ----------------------------------------------

yes_page = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Happy Birthday BBG!</title>

    <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Patrick+Hand&display=swap" rel="stylesheet">

    <style>
        body {
            background: linear-gradient(#ffdde9, #ffc1d6);
            font-family: 'Patrick Hand', cursive;
            text-align: center;
            padding-top: 150px;
            color: #ff2e84;
        }

        h1 {
            font-size: 50px;
            font-family: 'Pacifico', cursive;
        }

        .msg {
            font-size: 28px;
            width: 70%;
            margin: auto;
        }

        .heart {
            position: fixed;
            bottom: -50px;
            font-size: 26px;
            animation: floatUp 6s linear infinite;
            opacity: 0.85;
        }

        @keyframes floatUp {
            0% { transform: translateY(0) scale(1); opacity: 1; }
            100% { transform: translateY(-130vh) scale(1.9); opacity: 0; }
        }
    </style>
</head>

<body>

    <h1>Happy Birthday BBG 🎀💗✨</h1>

    <p class="msg">
        You are the sweetest, cutest, most precious human ever 💞  
        I’m so lucky to have you, even as my bestie 😭💗  
        Hope this year brings you all the happiness, love, and sparkles ✨  
        You deserve everything beautiful, my girl 💗🎀  
    </p>

    <script>
        function createHeart() {
            const heart = document.createElement("div");
            heart.classList.add("heart");
            heart.innerHTML = Math.random() > 0.5 ? "💖" : "💕";
            heart.style.left = Math.random() * 100 + "vw";
            heart.style.animationDuration = (4 + Math.random() * 3) + "s";
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 6000);
        }
        setInterval(createHeart, 400);
    </script>

</body>
</html>
"""

# ----------------------------------------------

no_page = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Not For You</title>

    <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Patrick+Hand&display=swap" rel="stylesheet">

    <style>
        body {
            background: #ffe1ef;
            text-align: center;
            padding-top: 160px;
            font-family: 'Patrick Hand', cursive;
            color: #ff4f9a;
        }

        h1 {
            font-size: 40px;
        }

        .heart {
            position: fixed;
            bottom: -50px;
            font-size: 24px;
            animation: floatUp 6s linear infinite;
            opacity: 0.8;
        }

        @keyframes floatUp {
            0% { transform: translateY(0) scale(1); opacity: 1; }
            100% { transform: translateY(-130vh) scale(1.8); opacity: 0; }
        }
    </style>
</head>

<body>

    <h1>This is only for my BBG &lt;3 💅✨</h1>

    <script>
        function createHeart() {
            const heart = document.createElement("div");
            heart.classList.add("heart");
            heart.innerHTML = Math.random() > 0.5 ? "💗" : "❤️";
            heart.style.left = Math.random() * 100 + "vw";
            heart.style.animationDuration = (4 + Math.random() * 4) + "s";
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 6000);
        }
        setInterval(createHeart, 500);
    </script>

</body>
</html>
"""

# ----------------------------------------------

@app.route("/")
def home():
    return render_template_string(main_page)

@app.route("/answer")
def answer():
    bbg = request.args.get("bbg")
    if bbg == "yes":
        return render_template_string(yes_page)
    else:
        return render_template_string(no_page)

# ----------------------------------------------

app.run(debug=False)
