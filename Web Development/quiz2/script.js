const questions = [
    {
      question: "How do you comment out multiple lines in JavaScript?",
      options: ["-- comment --", "/* comment */", "//", "// comment"],
      correctAnswer: "/* comment */"
  },
  {
      question: "Which HTML tag is used for creating a hyperlink?",
      options: ["<a>", "<hyperlink>", "<href>", "<link>"],
      correctAnswer: "<a>"
  },
  {
      question: "Which of the following tags is used for creating an unordered list?",
      options: ["<dl>", "<li>", "<ul>", "<ol>"],
      correctAnswer: "<ul>"
  },
  {
      question: "Which JavaScript keyword is used to declare a variable that cannot be reassigned?",
      options: ["static", "let", "const", "var"],
      correctAnswer: "const"
  },
  {
    question: "What is the capital of France?",
    options: ["Berlin", "Paris", "Madrid", "Rome"],
    correctAnswer: "Paris"
  },
  {
    question: "Which planet is known as the Red Planet?",
    options: ["Mars", "Venus", "Jupiter", "Saturn"],
    correctAnswer: "Mars"
  },
];

let currentQuestion = 0;
let score = 0;

let quizStarted = false;

// Modify the startQuiz function
function startQuiz() {
  quizStarted = true;

  // Display restart button instead of start button
  document.getElementById("start-btn").style.display = "none";
  document.getElementById("restart-btn").style.display = "block";

  // Show the next button
  document.getElementById("next-btn").style.display = "block";

  // Display the first question
  displayQuestion();
}



function displayQuestion() {
  const questionContainer = document.getElementById("question-container");
  const optionsContainer = document.getElementById("options-container");

  questionContainer.textContent = questions[currentQuestion].question;

  optionsContainer.innerHTML = "";
  questions[currentQuestion].options.forEach((option, index) => {
    const button = document.createElement("button");
    button.textContent = option;
    button.addEventListener("click", () => checkAnswer(option));
    optionsContainer.appendChild(button);
  });
}

function checkAnswer(selectedOption) {
  if (selectedOption === questions[currentQuestion].correctAnswer) {
    score++;
  }

  currentQuestion++;

  if (currentQuestion < questions.length) {
    displayQuestion();
  } else {
    displayResult();
  }
}

function displayResult() {
  const resultContainer = document.getElementById("result-container");
  const nextButton = document.getElementById("next-btn");

  resultContainer.textContent = `Your final score: ${score} out of ${questions.length}`;
  resultContainer.style.fontWeight = "bold";
  nextButton.style.display = "none";
}

function restartQuiz() {
  quizStarted = false;
  document.getElementById("start-btn").style.display = "block";
  document.getElementById("next-btn").style.display = "none";

}

function nextQuestion() {
if (!quizStarted) {
    return; // Do nothing if the quiz hasn't started
  }
  const resultContainer = document.getElementById("result-container");
  resultContainer.textContent = "";
  displayQuestion();
}

