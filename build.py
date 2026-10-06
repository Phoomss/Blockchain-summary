"""Build both reading layouts from the same Markdown sources."""
from pathlib import Path
import html
import re
import shutil
from urllib.parse import quote
import markdown

ROOT = Path(__file__).resolve().parent
SITE = ROOT / 'exam-site'
OUT = ROOT / 'dist'
OUT.mkdir(exist_ok=True)
core = (ROOT / 'สรุปสอบปลายภาค_เน้นอัตนัย.md').read_text(encoding='utf-8')
combined = core + '\n\n' + (SITE / 'deep-dive.md').read_text(encoding='utf-8')
chapters = re.split(r'^## ', combined, flags=re.M)[1:]
dark = (SITE / 'dark-template.html').read_text(encoding='utf-8')
markers = re.findall(r'\{\{CHAPTER_(\d+)\}\}', dark)
if len(chapters) != len(markers):
    raise ValueError('Update the dark layout sections when adding or removing chapters')

def render(text):
    return markdown.markdown(text, extensions=['tables', 'fenced_code', 'sane_lists'])

for index, chapter in enumerate(chapters, 1):
    body = render(chapter.split('\n', 1)[1])
    body = body.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
    dark = dark.replace('{{CHAPTER_' + str(index) + '}}', body)
(ROOT / 'index.html').write_text(dark.replace('{{LIGHT_URL}}', 'dist/index.html'), encoding='utf-8')
(OUT / 'dark.html').write_text(dark.replace('{{LIGHT_URL}}', 'index.html'), encoding='utf-8')

entries = []
def section(match):
    title = match.group(1)
    entries.append(html.unescape(re.sub('<.*?>', '', title)))
    index = len(entries)
    return f'<h2 id="chapter-{index}"><span class="chapter-no">บทที่ {index:02d}</span>{title}</h2>'

body = re.sub(r'<h1>.*?</h1>', '', render(combined), count=1)
body = re.sub(r'<h2>(.*?)</h2>', section, body)
body = body.replace('<table>', '<div class="table-scroll"><table>').replace('</table>', '</table></div>')
toc_parts = []
for i, title in enumerate(entries, 1):
    label = html.escape(re.sub(r'^\d+\.\s*', '', title))
    toc_parts.append(f'<a href="#chapter-{i}"><span>{i:02d}</span>{label}</a>')
toc = ''.join(toc_parts)
favicon = quote('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#15334c"/><path d="M7 8h7v7H7zm11 9h7v7h-7z" fill="#61dcc6"/><path d="M14 11h7v6M11 15v6h7" fill="none" stroke="white" stroke-width="2"/></svg>')
page = (SITE / 'light-template.html').read_text(encoding='utf-8')
page = page.replace('FAVICON', favicon).replace('TOC', toc).replace('BODY', body)
(OUT / 'index.html').write_text(page, encoding='utf-8')
(OUT / 'สรุปละเอียด_สอบปลายภาค.md').write_text(combined, encoding='utf-8')
shutil.copyfile(SITE / 'style.css', OUT / 'style.css')
print(f'Built both versions: {len(entries)} chapters from shared sources in {OUT}')
