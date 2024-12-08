import { LMStudioClient } from "@lmstudio/sdk";
import { readFile, readdir } from "fs/promises";
import { join } from "path";

// Adjust paths as needed
const finalReportPath = "C:\\Users\\qc_wo\\Desktop\\MAIN_APP\\final_report.md";
const reportsDirPath = "C:\\Users\\qc_wo\\Desktop\\MAIN_APP\\reports";

export async function answerQuestion(question) {
  const client = new LMStudioClient();

  // Upload final_report.md
  const finalReportHandle = await client.files.uploadTempFile(
    "final_report.md",
    await readFile(finalReportPath)
  );
  console.log("Uploaded final report:", finalReportHandle);

  // Load additional reports
  const reportFiles = await readdir(reportsDirPath);
  const mdReportFiles = reportFiles.filter(f => f.endsWith(".md"));
  const reportHandles = [];
  for (const file of mdReportFiles) {
    const fullPath = join(reportsDirPath, file);
    const handle = await client.files.uploadTempFile(
      file,
      await readFile(fullPath)
    );
    reportHandles.push(handle);
    console.log("Uploaded report:", handle, "Filename:", file);
  }

  const allHandles = [finalReportHandle, ...reportHandles];

  // Load embedding model
  const embeddingModel = await client.embedding.getOrLoad("text-embedding-nomic-embed-text-v1.5");
  console.log("Loaded embedding model:", embeddingModel);

  // Retrieve relevant documents
  const results = await client.retrieval.retrieve(question, allHandles, { embeddingModel });
  // console.log("Retrieval results:", results);

  if (!results.entries || results.entries.length === 0) {
    return "No relevant documents found.";
  }

  const topResult = results.entries[0].content;
  console.log("Top Retrieval Result:", topResult); // Log the top result

  const prompt = `
Answer the user's query using the information below:

----- Citation -----
${topResult}
----- End of Citation -----

User's question: ${question};
`;

  // Load LLM model
  // const llama = await client.llm.getOrLoad("qwen2.5-coder-7b-instruct:2");
  const llama = await client.llm.getOrLoad("llama-3.2-3b-qnn");
  // console.log("Loaded LLM model:", llama);

  let response = "";
  const prediction = llama.respond([
    { role: "user", content: prompt }
  ]);

  for await (const { content } of prediction) {
    response += content;
  }

  console.log("LLM Response:", response); // Log the LLM response

  return response.trim();
}