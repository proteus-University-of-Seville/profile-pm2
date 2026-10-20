# Renders the 48x48 flat icons of the PM2 classes from inline SVG.
# Usage: python tools/icons.py <icons folder> [preview.png], with the Python environment of PROTEUS (PyQt6).
import os, sys
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
from PyQt6.QtCore import QByteArray, Qt, QRectF
from PyQt6.QtGui import QGuiApplication, QImage, QPainter, QColor
from PyQt6.QtSvg import QSvgRenderer

ICONS = {
# clipboard with a form
"initiation-request": """
  <rect x="9" y="7" width="30" height="37" rx="3" fill="#0284C7"/>
  <rect x="13" y="12" width="22" height="28" rx="1" fill="#F8FAFC"/>
  <rect x="17" y="4" width="14" height="7" rx="2" fill="#475569"/>
  <rect x="17" y="18" width="14" height="2.5" fill="#7DD3FC"/>
  <rect x="17" y="24" width="14" height="2.5" fill="#7DD3FC"/>
  <rect x="17" y="30" width="9" height="2.5" fill="#7DD3FC"/>""",
# light bulb: need, problem or opportunity
"business-situation": """
  <path d="M24 5a13 13 0 0 0-7.5 23.6c1.6 1.2 2.5 3 2.5 5V35h10v-1.4c0-2 .9-3.8 2.5-5A13 13 0 0 0 24 5z" fill="#FB923C"/>
  <path d="M24 9a9 9 0 0 1 9 9" stroke="#FFEDD5" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <rect x="19" y="35" width="10" height="4" fill="#64748B"/>
  <rect x="20" y="39" width="8" height="4" rx="2" fill="#475569"/>""",
# target with an arrow
"strategic-goal": """
  <circle cx="22" cy="26" r="18" fill="#BE185D"/>
  <circle cx="22" cy="26" r="12.5" fill="#FCE7F3"/>
  <circle cx="22" cy="26" r="7" fill="#BE185D"/>
  <circle cx="22" cy="26" r="2.5" fill="#FCE7F3"/>
  <path d="M22 26L40 8" stroke="#334155" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M36 5l1 6 6 1-5 5-6-1-1-6z" fill="#F59E0B"/>""",
# scales of justice
"legal-basis": """
  <rect x="22.5" y="8" width="3" height="31" fill="#57534E"/>
  <rect x="14" y="38" width="20" height="5" rx="2" fill="#57534E"/>
  <rect x="7" y="11" width="34" height="3" rx="1.5" fill="#78716C"/>
  <path d="M5 28l6-14 6 14z" fill="none" stroke="#A8A29E" stroke-width="1.5"/>
  <path d="M31 28l6-14 6 14z" fill="none" stroke="#A8A29E" stroke-width="1.5"/>
  <path d="M4 28h14a7 5 0 0 1-14 0z" fill="#D97706"/>
  <path d="M30 28h14a7 5 0 0 1-14 0z" fill="#D97706"/>
  <circle cx="24" cy="8" r="3" fill="#D97706"/>""",
# flag on a pole
"outcome": """
  <rect x="9" y="5" width="3.5" height="39" rx="1.5" fill="#475569"/>
  <path d="M12.5 7h26l-6 8.5 6 8.5h-26z" fill="#65A30D"/>
  <path d="M12.5 7h26l-3 4.2h-23z" fill="#84CC16"/>""",
# waves of an impact
"impact": """
  <circle cx="24" cy="24" r="19" fill="#FEF3C7"/>
  <circle cx="24" cy="24" r="13" fill="#FCD34D"/>
  <circle cx="24" cy="24" r="7" fill="#D97706"/>""",
# trophy
"success-criterion": """
  <path d="M14 6h20v12a10 10 0 0 1-20 0z" fill="#16A34A"/>
  <path d="M14 9H7v4a7 7 0 0 0 8 7" fill="none" stroke="#16A34A" stroke-width="3"/>
  <path d="M34 9h7v4a7 7 0 0 1-8 7" fill="none" stroke="#16A34A" stroke-width="3"/>
  <rect x="21" y="27" width="6" height="8" fill="#15803D"/>
  <rect x="14" y="35" width="20" height="7" rx="2" fill="#475569"/>
  <path d="M19 15l3.5 3.5 7-7" fill="none" stroke="#DCFCE7" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>""",
# thought bubble: something taken as true
"assumption": """
  <ellipse cx="26" cy="20" rx="18" ry="14" fill="#0891B2"/>
  <circle cx="10" cy="37" r="4" fill="#0891B2"/>
  <circle cx="5" cy="44" r="2.5" fill="#0891B2"/>
  <path d="M20 15.5a6 6 0 1 1 7.5 5.8c-1 .4-1.5 1.2-1.5 2.2v1" fill="none" stroke="#ECFEFF" stroke-width="3.2" stroke-linecap="round"/>
  <circle cx="26" cy="29" r="2" fill="#ECFEFF"/>""",
# padlock
"constraint": """
  <path d="M15 21v-6a9 9 0 0 1 18 0v6" fill="none" stroke="#64748B" stroke-width="4"/>
  <rect x="9" y="20" width="30" height="24" rx="3" fill="#334155"/>
  <circle cx="24" cy="30" r="3.5" fill="#F8FAFC"/>
  <rect x="22.5" y="31" width="3" height="7" rx="1" fill="#F8FAFC"/>""",
# warning triangle
"risk": """
  <path d="M24 5L45 42H3z" fill="#DC2626" stroke="#DC2626" stroke-width="3" stroke-linejoin="round"/>
  <rect x="22" y="17" width="4" height="13" rx="2" fill="#FFFFFF"/>
  <circle cx="24" cy="35.5" r="2.4" fill="#FFFFFF"/>""",
# document with a shield
"document-control": """
  <path d="M9 4h20l9 9v31H9z" fill="#1E40AF"/>
  <path d="M29 4v9h9z" fill="#93C5FD"/>
  <rect x="13" y="12" width="12" height="2.5" fill="#BFDBFE"/>
  <rect x="13" y="18" width="18" height="2.5" fill="#BFDBFE"/>
  <path d="M31 24l9 3v7c0 5-4 8.5-9 10-5-1.5-9-5-9-10v-7z" fill="#F59E0B"/>
  <path d="M27 33.5l3 3 5.5-5.5" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>""",
# seal with a check mark
"approval": """
  <path d="M24 3l5 4 6.3-.6 1.9 6 5.3 3.5-2.2 5.9 2.2 5.9-5.3 3.5-1.9 6-6.3-.6-5 4-5-4-6.3.6-1.9-6-5.3-3.5 2.2-5.9-2.2-5.9 5.3-3.5 1.9-6 6.3.6z" fill="#2563EB"/>
  <path d="M16 23l5.5 5.5L33 17" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M15 37l-4 9 6-2 3 5 3-8z" fill="#1E40AF"/>
  <path d="M33 37l4 9-6-2-3 5-3-8z" fill="#1E40AF"/>""",
# clock with a back arrow: history
"revision": """
  <circle cx="25" cy="25" r="17" fill="#3B82F6"/>
  <circle cx="25" cy="25" r="13" fill="#EFF6FF"/>
  <path d="M25 16v9.5l6 4" fill="none" stroke="#1E40AF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M3 21l5-8 6 7z" fill="#1E40AF"/>""",
# --- Business Case ---
# three steps of a process
"business-process": """
  <rect x="3" y="18" width="12" height="12" rx="2.5" fill="#0F766E"/>
  <rect x="18" y="18" width="12" height="12" rx="2.5" fill="#14B8A6"/>
  <rect x="33" y="18" width="12" height="12" rx="2.5" fill="#0F766E"/>
  <path d="M15 24h3M30 24h3" stroke="#334155" stroke-width="2.5"/>
  <path d="M9 30v8h30v-8" fill="none" stroke="#5EEAD4" stroke-width="2.5"/>
  <path d="M35 34l4 4 4-4" fill="none" stroke="#5EEAD4" stroke-width="2.5" stroke-linejoin="round"/>""",
# signpost with two ways
"alternative": """
  <rect x="22" y="6" width="4" height="38" rx="1.5" fill="#475569"/>
  <path d="M8 9h24l6 5-6 5H8z" fill="#7E22CE"/>
  <path d="M40 22H16l-6 5 6 5h24z" fill="#C084FC"/>
  <rect x="17" y="42" width="14" height="3" rx="1.5" fill="#475569"/>""",
# bar chart with a rising arrow
"benefit": """
  <rect x="6" y="30" width="8" height="13" rx="1.5" fill="#6EE7B7"/>
  <rect x="18" y="23" width="8" height="20" rx="1.5" fill="#34D399"/>
  <rect x="30" y="15" width="8" height="28" rx="1.5" fill="#059669"/>
  <path d="M6 22L19 11l7 5L40 5" fill="none" stroke="#065F46" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M33 4h8v8" fill="none" stroke="#065F46" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>""",
# boundary with something inside and something outside
"scope-item": """
  <rect x="5" y="5" width="30" height="30" rx="4" fill="#E0E7FF" stroke="#4338CA" stroke-width="2.5" stroke-dasharray="5 3"/>
  <circle cx="20" cy="20" r="7" fill="#4338CA"/>
  <circle cx="39" cy="39" r="6" fill="#A5B4FC"/>""",
# parcel
"deliverable": """
  <path d="M24 4l19 9v22l-19 9-19-9V13z" fill="#D97706"/>
  <path d="M24 4l19 9-19 9-19-9z" fill="#FBBF24"/>
  <path d="M24 22v22" stroke="#B45309" stroke-width="2"/>
  <path d="M14 8.5l19 9v7" fill="none" stroke="#FEF3C7" stroke-width="3"/>""",
# diamond on a time line
"milestone": """
  <rect x="3" y="33" width="42" height="3" rx="1.5" fill="#94A3B8"/>
  <path d="M24 8l11 11-11 11-11-11z" fill="#DB2777"/>
  <rect x="22.5" y="30" width="3" height="9" fill="#DB2777"/>
  <circle cx="8" cy="34.5" r="3" fill="#64748B"/>
  <circle cx="40" cy="34.5" r="3" fill="#64748B"/>""",
# two chain links
"interdependency": """
  <rect x="4" y="16" width="24" height="16" rx="8" fill="none" stroke="#A21CAF" stroke-width="4.5"/>
  <rect x="20" y="16" width="24" height="16" rx="8" fill="none" stroke="#E879F9" stroke-width="4.5"/>
  <path d="M28 18.5a8 8 0 0 1 0 11" fill="none" stroke="#A21CAF" stroke-width="4.5"/>""",
# stack of coins
"cost-plan": """
  <ellipse cx="18" cy="36" rx="13" ry="5" fill="#A16207"/>
  <rect x="5" y="28" width="26" height="8" fill="#CA8A04"/>
  <ellipse cx="18" cy="28" rx="13" ry="5" fill="#FACC15"/>
  <rect x="5" y="20" width="26" height="8" fill="#CA8A04"/>
  <ellipse cx="18" cy="20" rx="13" ry="5" fill="#FDE047"/>
  <circle cx="35" cy="15" r="10" fill="#EAB308" stroke="#A16207" stroke-width="2"/>
  <path d="M38 11.5a4.5 4.5 0 1 0 0 7M30 14h6M30 16.5h6" fill="none" stroke="#713F12" stroke-width="1.8" stroke-linecap="round"/>""",
# receipt
"cost-item": """
  <path d="M10 4h28v40l-4.7-3-4.7 3-4.6-3-4.7 3-4.6-3L10 44z" fill="#CA8A04"/>
  <rect x="15" y="11" width="18" height="2.5" fill="#FEF9C3"/>
  <rect x="15" y="17" width="18" height="2.5" fill="#FEF9C3"/>
  <rect x="15" y="23" width="11" height="2.5" fill="#FEF9C3"/>
  <rect x="25" y="30" width="8" height="3" fill="#713F12"/>""",
}

def render(svg_body, size=48):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">{svg_body}</svg>'
    image = QImage(size, size, QImage.Format.Format_ARGB32)
    image.fill(Qt.GlobalColor.transparent)
    painter = QPainter(image)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    QSvgRenderer(QByteArray(svg.encode())).render(painter, QRectF(0, 0, size, size))
    painter.end()
    return image

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    out = sys.argv[1]
    for name, body in ICONS.items():
        assert render(body).save(os.path.join(out, f"{name}.png")), name
    if len(sys.argv) > 2:   # contact sheet at 2x to review the icons
        sheet = QImage(len(ICONS) * 104, 104, QImage.Format.Format_ARGB32)
        sheet.fill(QColor("white"))
        p = QPainter(sheet)
        for i, body in enumerate(ICONS.values()):
            p.drawImage(i * 104 + 4, 4, render(body, 96))
        p.end()
        sheet.save(sys.argv[2])
    print(len(ICONS), "icons")
