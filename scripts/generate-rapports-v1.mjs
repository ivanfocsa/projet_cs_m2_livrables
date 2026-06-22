import fs from "node:fs";
import path from "node:path";
import PDFDocument from "pdfkit";

const root = process.cwd();

const reports = [
  {
    source: path.join(root, "livrables", "rapport-final", "rapport-technique-final-50p-v1.md"),
    output: path.join(root, "livrables", "rapport-final", "Rapport_Technique_Final_50p_V1_SANS_PAGES_BLANCHES.pdf"),
    title: "Rapport technique final - version consolidee",
    subtitle: "SOC externalise pour un reseau d'audioprothesistes",
  },
  {
    source: path.join(root, "livrables", "individuels", "Yvan_FOCSA_rendu_individuel_v1.md"),
    output: path.join(root, "livrables", "individuels", "Yvan_FOCSA_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf"),
    title: "Rendu individuel - Yvan FOCSA - V1",
    subtitle: "Architecture securite, infrastructure et industrialisation",
  },
  {
    source: path.join(root, "livrables", "individuels", "Kilyan_FELIX_rendu_individuel_v1.md"),
    output: path.join(root, "livrables", "individuels", "Kilyan_FELIX_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf"),
    title: "Rendu individuel - Kilyan FELIX - V1",
    subtitle: "Pilotage projet, cadrage client et coherence des livrables",
  },
  {
    source: path.join(root, "livrables", "individuels", "Youssef_GUERNIOU_rendu_individuel_v1.md"),
    output: path.join(root, "livrables", "individuels", "Youssef_GUERNIOU_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf"),
    title: "Rendu individuel - Youssef GUERNIOU - V1",
    subtitle: "Ingenierie SIEM, Wazuh, collecte et dashboards",
  },
  {
    source: path.join(root, "livrables", "individuels", "Mahamadou_DIACOUMBA_rendu_individuel_v1.md"),
    output: path.join(root, "livrables", "individuels", "Mahamadou_DIACOUMBA_Rendu_Individuel_V1_SANS_PAGES_BLANCHES.pdf"),
    title: "Rendu individuel - Mahamadou DIACOUMBA - V1",
    subtitle: "Detection SOC, regles, playbooks et REX incidents",
  },
];

const colors = {
  ink: "#172033",
  muted: "#667085",
  line: "#D9DEE8",
  soft: "#F5F7FB",
  blue: "#2457D6",
  white: "#FFFFFF",
};

const layout = {
  x: 54,
  top: 54,
  bottom: 64,
  width: 487,
};

function stripMarkdownInline(value) {
  return value
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/<br\/>/g, " / ")
    .trim();
}

function addFooter(doc, pageNo) {
  // Intentionally empty: footers caused blank trailing pages in some PDF viewers.
}

function newPage(doc, state) {
  addFooter(doc, state.pageNo);
  doc.addPage();
  state.pageNo += 1;
  doc.y = layout.top;
}

function ensureLine(doc, state, lineHeight) {
  if (doc.y + lineHeight > doc.page.height - layout.bottom) {
    newPage(doc, state);
  }
}

function wrapText(doc, value, width, fontName, size) {
  const text = stripMarkdownInline(value);
  if (!text) return [];

  doc.font(fontName).fontSize(size);
  const words = text.split(/\s+/);
  const lines = [];
  let current = "";

  for (const word of words) {
    const test = current ? `${current} ${word}` : word;
    if (doc.widthOfString(test) <= width) {
      current = test;
      continue;
    }

    if (current) {
      lines.push(current);
      current = "";
    }

    if (doc.widthOfString(word) <= width) {
      current = word;
      continue;
    }

    let chunk = "";
    for (const char of word) {
      const testChunk = chunk + char;
      if (doc.widthOfString(testChunk) <= width) {
        chunk = testChunk;
      } else {
        if (chunk) lines.push(chunk);
        chunk = char;
      }
    }
    current = chunk;
  }

  if (current) lines.push(current);
  return lines;
}

function writeWrapped(doc, state, value, options = {}) {
  const x = options.x ?? layout.x;
  const width = options.width ?? layout.width;
  const size = options.size ?? 10;
  const fontName = options.bold ? "Helvetica-Bold" : options.font ?? "Helvetica";
  const color = options.color ?? colors.ink;
  const lineHeight = options.lineHeight ?? size + 4;
  const after = options.after ?? 4;
  const lines = wrapText(doc, value, width, fontName, size);

  for (const line of lines) {
    ensureLine(doc, state, lineHeight);
    if (options.background) {
      doc.roundedRect(x - 5, doc.y - 2, width + 10, lineHeight + 2, 3).fill(colors.soft);
    }
    doc
      .font(fontName)
      .fontSize(size)
      .fillColor(color)
      .text(line, x, doc.y, { lineBreak: false });
    doc.y += lineHeight;
  }
  doc.y += after;
}

function renderHeading(doc, state, line) {
  const [, marks, rawTitle] = line.match(/^(#{1,3})\s+(.*)$/);
  const level = marks.length;
  const size = level === 1 ? 17 : level === 2 ? 13 : 11;
  const before = level === 1 ? 10 : 7;

  doc.y += before;
  writeWrapped(doc, state, rawTitle, {
    size,
    bold: true,
    color: level === 1 ? colors.blue : colors.ink,
    lineHeight: size + 5,
    after: level === 1 ? 8 : 5,
  });
}

function renderTable(doc, state, rows) {
  const cleanRows = rows.filter((line) => !/^\|\s*-+/.test(line));
  for (const row of cleanRows) {
    const text = row
      .split("|")
      .slice(1, -1)
      .map((cell) => stripMarkdownInline(cell))
      .join(" | ");

    writeWrapped(doc, state, text, {
      font: "Courier",
      size: 7.1,
      lineHeight: 9.4,
      after: 1,
    });
  }
  doc.y += 5;
}

function renderCodeBlock(doc, state, lines) {
  for (const line of lines) {
    writeWrapped(doc, state, line || " ", {
      font: "Courier",
      size: 7.1,
      lineHeight: 9.4,
      after: 0,
      background: true,
    });
  }
  doc.y += 6;
}

function renderMarkdownPdf({ source, output, title, subtitle }) {
  const markdown = fs.readFileSync(source, "utf8").replace(/\r\n/g, "\n");
  fs.mkdirSync(path.dirname(output), { recursive: true });

  const doc = new PDFDocument({
    size: "A4",
    margin: 42,
    bufferPages: false,
    info: {
      Title: title,
      Author: "Yvan FOCSA, Youssef GUERNIOU, Kilyan FELIX, Mahamadou DIACOUMBA",
    },
  });

  doc.pipe(fs.createWriteStream(output));
  const state = { pageNo: 1 };

  doc.rect(0, 0, doc.page.width, 128).fill(colors.blue);
  doc
    .font("Helvetica-Bold")
    .fontSize(24)
    .fillColor(colors.white)
    .text(title, 42, 44, { width: doc.page.width - 84, lineBreak: false });
  doc
    .font("Helvetica")
    .fontSize(11)
    .fillColor(colors.white)
    .text(subtitle, 42, 82, { width: doc.page.width - 84, lineBreak: false });
  doc.y = 154;

  const lines = markdown.split("\n");
  let paragraph = [];
  let table = [];
  let code = [];
  let inCode = false;

  function flushParagraph() {
    if (!paragraph.length) return;
    writeWrapped(doc, state, paragraph.join(" "), { size: 10, lineHeight: 14, after: 6 });
    paragraph = [];
  }

  function flushTable() {
    if (!table.length) return;
    renderTable(doc, state, table);
    table = [];
  }

  function flushCode() {
    if (!code.length) return;
    renderCodeBlock(doc, state, code);
    code = [];
  }

  for (const raw of lines) {
    const line = raw.trimEnd();

    if (line.startsWith("```")) {
      flushParagraph();
      flushTable();
      if (inCode) {
        flushCode();
        inCode = false;
      } else {
        inCode = true;
      }
      continue;
    }

    if (inCode) {
      code.push(line);
      continue;
    }

    if (line.trim() === "<!-- pagebreak -->") {
      flushParagraph();
      flushTable();
      flushCode();
      newPage(doc, state);
      continue;
    }

    if (!line.trim()) {
      flushParagraph();
      flushTable();
      continue;
    }

    if (line.startsWith("|")) {
      flushParagraph();
      table.push(line);
      continue;
    }

    flushTable();

    if (/^#{1,3}\s+/.test(line)) {
      flushParagraph();
      renderHeading(doc, state, line);
      continue;
    }

    if (line.startsWith("- ")) {
      flushParagraph();
      writeWrapped(doc, state, `- ${line.slice(2)}`, {
        x: layout.x + 12,
        width: layout.width - 12,
        size: 10,
        lineHeight: 14,
        after: 2,
      });
      continue;
    }

    if (/^\d+\.\s+/.test(line)) {
      flushParagraph();
      writeWrapped(doc, state, line, {
        x: layout.x + 12,
        width: layout.width - 12,
        size: 10,
        lineHeight: 14,
        after: 2,
      });
      continue;
    }

    paragraph.push(line);
  }

  flushParagraph();
  flushTable();
  flushCode();
  addFooter(doc, state.pageNo);
  doc.end();
}

for (const report of reports) {
  renderMarkdownPdf(report);
  console.log(`Generated ${path.relative(root, report.output)}`);
}
