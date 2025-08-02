function toggleChatbot() {
    alert("Connect Whatsapp");
    // You can replace this with an actual chatbot UI or integration
  }

  document.getElementById("download-cert").addEventListener("click", function (event) {
    event.preventDefault();

    const images = [
      {
        href: "./assets/img/cer1.png",
        filename: "Professional-Certificate-1.jpeg"
      },
      {
        href: "./assets/img/cer2.png",
        filename: "Professional-Certificate-2.jpeg"
      }
    ];

    // Recursive function to trigger download with a delay
    function downloadImage(index) {
      if (index >= images.length) return;

      const img = images[index];
      const link = document.createElement("a");
      link.href = img.href;
      link.download = img.filename;

      // Required for some browsers (e.g., Firefox)
      link.style.display = "none";
      document.body.appendChild(link);

      // Trigger download
      link.click();

      // Cleanup
      document.body.removeChild(link);

      // Delay next download
      setTimeout(() => downloadImage(index + 1), 500);
    }

    // Start download
    downloadImage(0);
  });

  new PerformanceObserver((entryList) => {
    for (const entry of entryList.getEntries()) {
      console.log('LCP candidate:', entry);
    }
  }).observe({ type: 'largest-contentful-paint', buffered: true });