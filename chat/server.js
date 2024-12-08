import express from "express";
import path from "path";
import { fileURLToPath } from "url";
import { answerQuestion } from "./rag.js";

// For ESM __dirname
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(express.json());

// Serve static frontend
app.use(express.static(path.join(__dirname, "public")));

app.post("/ask", async (req, res) => {
  const { question } = req.body;
  if (!question || typeof question !== "string") {
    return res.status(400).json({ error: "Invalid question." });
  }

  try {
    const answer = await answerQuestion(question);
    res.json({ answer });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Error generating answer." });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
