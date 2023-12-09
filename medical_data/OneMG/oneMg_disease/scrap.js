const puppeteer = require("puppeteer");
const fs = require("fs");

async function scrapeDataFromLink(url) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url);

  const data = await page.evaluate(() => {
    const divElements = document.querySelectorAll("div.style_dynamic-widget__39jlH");
    const paragraphs = [];

    divElements.forEach((divElement) => {
      const pTags = divElement.querySelectorAll("p");
      pTags.forEach((pTag) => {
        paragraphs.push(pTag.innerText);
      });
    });

    return paragraphs;
  });

  await browser.close();
  return data;
}

async function crawlAndScrape() {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto("https://www.1mg.com/all-diseases");
  
    const links = await page.evaluate(() => {
      const divElements = document.querySelectorAll("div.style_width-100p__2woP5"); // Replace "your-target-class" with the appropriate class name or selector for the div containing the <a> tags
  
      const hrefs = [];
  
      divElements.forEach((divElement) => {
        const anchorElements = divElement.querySelectorAll("a"); // Select all <a> tags within the div
        anchorElements.forEach((anchor) => {
          hrefs.push(anchor.href); // Extract the "href" attribute of each <a> tag and push it to the array
        });
      });
  
      return hrefs;
    });

  await browser.close();

  const allData = [];

  for (const link of links) {
    const data = await scrapeDataFromLink(link);
    allData.push(data);
  }

  return allData;
}

crawlAndScrape()
  .then((allData) => {
    const filePath = "scraped_data.txt";
    let content = "";

    allData.forEach((data, index) => {
      content += `Data from Link ${index + 1}:\n${data.join("\n")}\n\n`;
    });

    fs.writeFile(filePath, content, (err) => {
      if (err) {
        console.error("Error writing the file:", err);
      } else {
        console.log("Data successfully written to", filePath);
      }
    });
  })
  .catch((err) => {
    console.error("Error crawling and scraping:", err);
  });