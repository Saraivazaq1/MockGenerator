document.getElementById("baixar-btn").addEventListener("click", () => {
    const link = document.createElement("a");
    link.href = "/gerar-csv";
    link.download = "mockInfo.csv";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  });