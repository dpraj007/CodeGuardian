import express from "express";
import { answerQuestion } from "./rag.js";
import path from "path";
const app = express();
app.use(express.json());
// Serve static frontend
app.use(express.static(path.join(process.cwd(), "public")));
app.post("/ask", async (req, res) => {
    const question = req.body.question;
    if (!question || typeof question !== "string") {
        return res.status(400).json({ error: "Invalid question." });
    }
    try {
        const answer = await answerQuestion(question);
        res.json({ answer });
    }
    catch (err) {
        console.error(err);
        res.status(500).json({ error: "Error generating answer." });
    }
});
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
