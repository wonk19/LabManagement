#!/usr/bin/env python3
"""Generate the LabManagement index.html dashboard page."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "index.html"

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Lab Management</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" rel="stylesheet" />
  <style>
    :root {
      --bg0: #0f1c24;
      --bg1: #162a35;
      --bg2: #1d3644;
      --panel: rgba(245, 248, 250, 0.94);
      --panel-border: rgba(22, 42, 53, 0.12);
      --ink: #13232c;
      --muted: #5b6f7a;
      --line: #d5dee4;
      --accent: #1f7a6c;
      --accent-soft: #d7efe9;
      --warn: #b45309;
      --danger: #b42318;
      --day-head: #e8eef2;
      --today: #c7ebe3;
      --shadow: 0 10px 30px rgba(8, 20, 28, 0.18);
      --radius: 14px;
      --font-ui: "IBM Plex Sans", sans-serif;
      --font-display: "Source Serif 4", Georgia, serif;
    }

    * { box-sizing: border-box; }

    html, body {
      margin: 0;
      min-height: 100%;
      font-family: var(--font-ui);
      color: var(--ink);
      background:
        radial-gradient(1200px 600px at 10% -10%, #2a5d55 0%, transparent 55%),
        radial-gradient(900px 500px at 100% 0%, #3a4f6b 0%, transparent 50%),
        linear-gradient(160deg, var(--bg0), var(--bg1) 45%, var(--bg2));
    }

    body {
      padding: 18px;
    }

    .app {
      max-width: 1400px;
      margin: 0 auto;
      display: grid;
      grid-template-rows: auto minmax(280px, 1fr);
      gap: 14px;
      min-height: calc(100vh - 36px);
    }

    .panel {
      background: var(--panel);
      border: 1px solid var(--panel-border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      min-height: 0;
    }

    .panel-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 14px 16px 10px;
      border-bottom: 1px solid var(--line);
      background: linear-gradient(180deg, #fbfcfd, #f1f5f7);
    }

    .panel-head h1,
    .panel-head h2 {
      margin: 0;
      font-family: var(--font-display);
      font-weight: 700;
      letter-spacing: -0.02em;
    }

    .panel-head h1 { font-size: 1.35rem; }
    .panel-head h2 { font-size: 1.05rem; }

    .panel-sub {
      margin: 4px 0 0;
      color: var(--muted);
      font-size: 0.82rem;
    }

    .toolbar {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }

    button, .btn {
      appearance: none;
      border: 1px solid transparent;
      border-radius: 8px;
      padding: 7px 11px;
      font: 500 0.82rem var(--font-ui);
      cursor: pointer;
      background: var(--accent);
      color: #fff;
      transition: transform 0.12s ease, filter 0.12s ease, background 0.12s ease;
    }

    button:hover, .btn:hover { filter: brightness(1.05); }
    button:active, .btn:active { transform: translateY(1px); }
    button.ghost {
      background: #fff;
      color: var(--ink);
      border-color: var(--line);
    }
    button.danger { background: var(--danger); }

    .calendar-body {
      padding: 12px 14px 16px;
      overflow: auto;
    }

    .week-block {
      margin-bottom: 12px;
    }

    .week-label {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin: 0 0 8px;
      font-size: 0.86rem;
      color: var(--muted);
      font-weight: 600;
    }

    .week-grid {
      display: grid;
      grid-template-columns: repeat(7, minmax(0, 1fr));
      gap: 6px;
    }

    .day {
      min-height: 118px;
      border: 1px solid var(--line);
      border-radius: 10px;
      background: #fff;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }

    .day.today {
      border-color: var(--accent);
      box-shadow: inset 0 0 0 1px rgba(31, 122, 108, 0.25);
    }

    .day-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 6px 8px;
      background: var(--day-head);
      border-bottom: 1px solid var(--line);
      font-size: 0.75rem;
      font-weight: 600;
    }

    .day.today .day-head { background: var(--today); }

    .day-date { color: var(--muted); font-weight: 500; }

    .day-events {
      flex: 1;
      padding: 6px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      min-height: 0;
      overflow: auto;
    }

    .event-chip {
      border: none;
      border-radius: 6px;
      padding: 5px 7px;
      text-align: left;
      background: var(--accent-soft);
      color: #0f4a42;
      font-size: 0.74rem;
      font-weight: 600;
      line-height: 1.25;
      width: 100%;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .event-chip .time {
      display: block;
      font-weight: 500;
      opacity: 0.8;
      font-size: 0.68rem;
    }

    .day-add {
      margin-top: auto;
      border: 1px dashed #b9c7cf;
      background: transparent;
      color: var(--muted);
      padding: 4px 6px;
      font-size: 0.72rem;
      border-radius: 6px;
    }

    .day-add:hover {
      background: #f3f7f9;
      color: var(--ink);
      filter: none;
    }

    .bottom {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      min-height: 0;
    }

    .table-wrap {
      padding: 10px 12px 14px;
      overflow: auto;
      flex: 1;
      min-height: 0;
    }

    table.data {
      width: 100%;
      border-collapse: collapse;
      table-layout: fixed;
      font-size: 0.84rem;
    }

    table.data th,
    table.data td {
      border: 1px solid var(--line);
      padding: 0;
      vertical-align: top;
    }

    table.data th {
      background: #eef3f6;
      color: var(--muted);
      font-weight: 600;
      text-align: left;
      padding: 8px 10px;
      position: sticky;
      top: 0;
      z-index: 1;
    }

    table.data td[contenteditable="true"] {
      padding: 8px 10px;
      outline: none;
      background: #fff;
      min-height: 34px;
      word-break: break-word;
    }

    table.data td[contenteditable="true"]:focus {
      box-shadow: inset 0 0 0 2px rgba(31, 122, 108, 0.35);
      background: #f7fcfb;
    }

    table.data td.actions {
      width: 44px;
      text-align: center;
      vertical-align: middle;
      background: #fafbfc;
    }

    table.data td.actions button {
      padding: 4px 7px;
      background: transparent;
      color: var(--danger);
      border: 1px solid transparent;
    }

    table.data td.actions button:hover {
      border-color: #f0c7c3;
      background: #fff5f4;
      filter: none;
    }

    .status {
      font-size: 0.75rem;
      color: var(--muted);
      min-height: 1em;
    }

    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(8, 18, 24, 0.45);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
      z-index: 50;
    }

    .modal-backdrop.open { display: flex; }

    .modal {
      width: min(420px, 100%);
      background: #fff;
      border-radius: 12px;
      box-shadow: var(--shadow);
      padding: 16px;
    }

    .modal h3 {
      margin: 0 0 12px;
      font-family: var(--font-display);
      font-size: 1.15rem;
    }

    .field {
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-bottom: 10px;
    }

    .field label {
      font-size: 0.78rem;
      color: var(--muted);
      font-weight: 600;
    }

    .field input {
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 8px 10px;
      font: 500 0.9rem var(--font-ui);
    }

    .modal-actions {
      display: flex;
      justify-content: flex-end;
      gap: 8px;
      margin-top: 8px;
    }

    @media (max-width: 980px) {
      .app { grid-template-rows: auto auto; }
      .bottom { grid-template-columns: 1fr; }
      .week-grid { min-width: 720px; }
    }
  </style>
</head>
<body>
  <div class="app">
    <section class="panel" id="calendar-panel">
      <div class="panel-head">
        <div>
          <h1>Lab Schedule</h1>
          <p class="panel-sub" id="range-label">Two-week overview</p>
        </div>
        <div class="toolbar">
          <button type="button" class="ghost" id="btn-prev-week">Prev week</button>
          <button type="button" class="ghost" id="btn-today">This week</button>
          <button type="button" class="ghost" id="btn-next-week">Next week</button>
          <button type="button" id="btn-add-event">Add event</button>
          <span class="status" id="cal-status"></span>
        </div>
      </div>
      <div class="calendar-body" id="calendar-root"></div>
    </section>

    <div class="bottom">
      <section class="panel">
        <div class="panel-head">
          <div>
            <h2>Research Deadlines</h2>
            <p class="panel-sub">Project / task / due date / student</p>
          </div>
          <div class="toolbar">
            <button type="button" class="ghost" data-add-row="research">Add row</button>
            <span class="status" id="research-status"></span>
          </div>
        </div>
        <div class="table-wrap">
          <table class="data" id="research-table">
            <thead>
              <tr>
                <th>Project</th>
                <th>Task</th>
                <th>Due date</th>
                <th>Student</th>
                <th style="width:44px"></th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </section>

      <section class="panel">
        <div class="panel-head">
          <div>
            <h2>Admin / Event Deadlines</h2>
            <p class="panel-sub">Item / task / due date / owner</p>
          </div>
          <div class="toolbar">
            <button type="button" class="ghost" data-add-row="admin">Add row</button>
            <span class="status" id="admin-status"></span>
          </div>
        </div>
        <div class="table-wrap">
          <table class="data" id="admin-table">
            <thead>
              <tr>
                <th>Item</th>
                <th>Task</th>
                <th>Due date</th>
                <th>Owner</th>
                <th style="width:44px"></th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </section>
    </div>
  </div>

  <div class="modal-backdrop" id="event-modal" aria-hidden="true">
    <div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <h3 id="modal-title">Event</h3>
      <div class="field">
        <label for="ev-title">Title</label>
        <input id="ev-title" type="text" maxlength="120" />
      </div>
      <div class="field">
        <label for="ev-date">Date</label>
        <input id="ev-date" type="date" />
      </div>
      <div class="field">
        <label for="ev-time">Time (optional)</label>
        <input id="ev-time" type="time" />
      </div>
      <div class="modal-actions">
        <button type="button" class="ghost" id="ev-cancel">Cancel</button>
        <button type="button" class="danger" id="ev-delete" hidden>Delete</button>
        <button type="button" id="ev-save">Save</button>
      </div>
    </div>
  </div>

  <script>
    (function () {
      var STORAGE_KEY = "labmgmt_dashboard_v1";
      var DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
      var ROW_COUNT = 7;

      var state = {
        weekOffset: 0,
        events: [],
        research: [],
        admin: [],
        editEventId: null
      };

      function uid() {
        return "id_" + Date.now().toString(36) + "_" + Math.random().toString(36).slice(2, 8);
      }

      function pad(n) {
        return String(n).padStart(2, "0");
      }

      function toISODate(d) {
        return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate());
      }

      function parseISODate(s) {
        var p = String(s || "").split("-");
        if (p.length !== 3) return null;
        var d = new Date(Number(p[0]), Number(p[1]) - 1, Number(p[2]));
        return isNaN(d.getTime()) ? null : d;
      }

      function startOfWeek(date) {
        var d = new Date(date.getFullYear(), date.getMonth(), date.getDate());
        var day = d.getDay();
        var diff = day === 0 ? -6 : 1 - day;
        d.setDate(d.getDate() + diff);
        return d;
      }

      function addDays(date, n) {
        var d = new Date(date.getFullYear(), date.getMonth(), date.getDate());
        d.setDate(d.getDate() + n);
        return d;
      }

      function emptyRows(n) {
        var rows = [];
        for (var i = 0; i < n; i++) {
          rows.push({ c0: "", c1: "", c2: "", c3: "" });
        }
        return rows;
      }

      function loadState() {
        try {
          var raw = localStorage.getItem(STORAGE_KEY);
          if (!raw) {
            state.events = [];
            state.research = emptyRows(ROW_COUNT);
            state.admin = emptyRows(ROW_COUNT);
            return;
          }
          var data = JSON.parse(raw);
          state.events = Array.isArray(data.events) ? data.events : [];
          state.research = Array.isArray(data.research) && data.research.length
            ? data.research
            : emptyRows(ROW_COUNT);
          state.admin = Array.isArray(data.admin) && data.admin.length
            ? data.admin
            : emptyRows(ROW_COUNT);
        } catch (e) {
          state.events = [];
          state.research = emptyRows(ROW_COUNT);
          state.admin = emptyRows(ROW_COUNT);
        }
      }

      function saveState(statusId) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify({
          events: state.events,
          research: state.research,
          admin: state.admin
        }));
        if (statusId) {
          var el = document.getElementById(statusId);
          if (el) {
            el.textContent = "Saved";
            clearTimeout(el._t);
            el._t = setTimeout(function () { el.textContent = ""; }, 1200);
          }
        }
      }

      function eventsOn(iso) {
        return state.events
          .filter(function (ev) { return ev.date === iso; })
          .sort(function (a, b) {
            return String(a.time || "").localeCompare(String(b.time || ""));
          });
      }

      function renderCalendar() {
        var root = document.getElementById("calendar-root");
        var base = addDays(startOfWeek(new Date()), state.weekOffset * 7);
        var todayIso = toISODate(new Date());
        var end = addDays(base, 13);
        document.getElementById("range-label").textContent =
          "Showing " + toISODate(base) + " to " + toISODate(end);

        var html = "";
        for (var w = 0; w < 2; w++) {
          var weekStart = addDays(base, w * 7);
          var weekEnd = addDays(weekStart, 6);
          html += '<div class="week-block">';
          html += '<div class="week-label"><span>Week ' + (w + 1) + '</span>';
          html += "<span>" + toISODate(weekStart) + " - " + toISODate(weekEnd) + "</span></div>";
          html += '<div class="week-grid">';
          for (var i = 0; i < 7; i++) {
            var day = addDays(weekStart, i);
            var iso = toISODate(day);
            var isToday = iso === todayIso;
            html += '<div class="day' + (isToday ? " today" : "") + '" data-date="' + iso + '">';
            html += '<div class="day-head"><span>' + DAY_NAMES[i] + '</span>';
            html += '<span class="day-date">' + pad(day.getMonth() + 1) + "/" + pad(day.getDate()) + "</span></div>";
            html += '<div class="day-events">';
            var list = eventsOn(iso);
            for (var e = 0; e < list.length; e++) {
              var ev = list[e];
              html += '<button type="button" class="event-chip" data-edit-id="' + ev.id + '">';
              if (ev.time) html += '<span class="time">' + ev.time + "</span>";
              html += escapeHtml(ev.title || "(untitled)") + "</button>";
            }
            html += '<button type="button" class="day-add" data-add-date="' + iso + '">+ Add</button>';
            html += "</div></div>";
          }
          html += "</div></div>";
        }
        root.innerHTML = html;
      }

      function escapeHtml(s) {
        return String(s)
          .replace(/&/g, "&amp;")
          .replace(/</g, "&lt;")
          .replace(/>/g, "&gt;")
          .replace(/"/g, "&quot;");
      }

      function readTable(kind) {
        var table = document.getElementById(kind + "-table");
        var rows = [];
        var trs = table.tBodies[0].rows;
        for (var i = 0; i < trs.length; i++) {
          var cells = trs[i].querySelectorAll('[contenteditable="true"]');
          rows.push({
            c0: (cells[0] && cells[0].textContent || "").trim(),
            c1: (cells[1] && cells[1].textContent || "").trim(),
            c2: (cells[2] && cells[2].textContent || "").trim(),
            c3: (cells[3] && cells[3].textContent || "").trim()
          });
        }
        return rows;
      }

      function renderTable(kind) {
        var table = document.getElementById(kind + "-table");
        var rows = state[kind];
        var html = "";
        for (var i = 0; i < rows.length; i++) {
          var r = rows[i];
          html += "<tr>";
          html += '<td contenteditable="true" data-col="0">' + escapeHtml(r.c0) + "</td>";
          html += '<td contenteditable="true" data-col="1">' + escapeHtml(r.c1) + "</td>";
          html += '<td contenteditable="true" data-col="2">' + escapeHtml(r.c2) + "</td>";
          html += '<td contenteditable="true" data-col="3">' + escapeHtml(r.c3) + "</td>";
          html += '<td class="actions"><button type="button" data-del-row="' + kind + '" data-idx="' + i + '" title="Remove row">x</button></td>';
          html += "</tr>";
        }
        table.tBodies[0].innerHTML = html;
      }

      function persistTable(kind) {
        state[kind] = readTable(kind);
        saveState(kind + "-status");
      }

      function openModal(opts) {
        state.editEventId = opts.id || null;
        document.getElementById("modal-title").textContent = opts.id ? "Edit event" : "Add event";
        document.getElementById("ev-title").value = opts.title || "";
        document.getElementById("ev-date").value = opts.date || toISODate(new Date());
        document.getElementById("ev-time").value = opts.time || "";
        document.getElementById("ev-delete").hidden = !opts.id;
        var modal = document.getElementById("event-modal");
        modal.classList.add("open");
        modal.setAttribute("aria-hidden", "false");
        document.getElementById("ev-title").focus();
      }

      function closeModal() {
        var modal = document.getElementById("event-modal");
        modal.classList.remove("open");
        modal.setAttribute("aria-hidden", "true");
        state.editEventId = null;
      }

      function bindEvents() {
        document.getElementById("btn-prev-week").addEventListener("click", function () {
          state.weekOffset -= 1;
          renderCalendar();
        });
        document.getElementById("btn-next-week").addEventListener("click", function () {
          state.weekOffset += 1;
          renderCalendar();
        });
        document.getElementById("btn-today").addEventListener("click", function () {
          state.weekOffset = 0;
          renderCalendar();
        });
        document.getElementById("btn-add-event").addEventListener("click", function () {
          openModal({ date: toISODate(new Date()) });
        });

        document.getElementById("calendar-root").addEventListener("click", function (e) {
          var editBtn = e.target.closest("[data-edit-id]");
          if (editBtn) {
            var id = editBtn.getAttribute("data-edit-id");
            var ev = state.events.find(function (x) { return x.id === id; });
            if (ev) openModal(ev);
            return;
          }
          var addBtn = e.target.closest("[data-add-date]");
          if (addBtn) {
            openModal({ date: addBtn.getAttribute("data-add-date") });
          }
        });

        document.getElementById("ev-cancel").addEventListener("click", closeModal);
        document.getElementById("event-modal").addEventListener("click", function (e) {
          if (e.target === e.currentTarget) closeModal();
        });

        document.getElementById("ev-save").addEventListener("click", function () {
          var title = document.getElementById("ev-title").value.trim();
          var date = document.getElementById("ev-date").value;
          var time = document.getElementById("ev-time").value;
          if (!title) {
            document.getElementById("ev-title").focus();
            return;
          }
          if (!parseISODate(date)) {
            document.getElementById("ev-date").focus();
            return;
          }
          if (state.editEventId) {
            var found = state.events.find(function (x) { return x.id === state.editEventId; });
            if (found) {
              found.title = title;
              found.date = date;
              found.time = time;
            }
          } else {
            state.events.push({ id: uid(), title: title, date: date, time: time });
          }
          saveState("cal-status");
          closeModal();
          renderCalendar();
        });

        document.getElementById("ev-delete").addEventListener("click", function () {
          if (!state.editEventId) return;
          state.events = state.events.filter(function (x) { return x.id !== state.editEventId; });
          saveState("cal-status");
          closeModal();
          renderCalendar();
        });

        document.querySelectorAll("[data-add-row]").forEach(function (btn) {
          btn.addEventListener("click", function () {
            var kind = btn.getAttribute("data-add-row");
            persistTable(kind);
            state[kind].push({ c0: "", c1: "", c2: "", c3: "" });
            renderTable(kind);
            saveState(kind + "-status");
          });
        });

        ["research", "admin"].forEach(function (kind) {
          var table = document.getElementById(kind + "-table");
          table.addEventListener("input", function () {
            persistTable(kind);
          });
          table.addEventListener("click", function (e) {
            var btn = e.target.closest("[data-del-row]");
            if (!btn) return;
            var idx = Number(btn.getAttribute("data-idx"));
            persistTable(kind);
            if (state[kind].length <= 1) {
              state[kind][0] = { c0: "", c1: "", c2: "", c3: "" };
            } else {
              state[kind].splice(idx, 1);
            }
            renderTable(kind);
            saveState(kind + "-status");
          });
        });

        document.addEventListener("keydown", function (e) {
          if (e.key === "Escape") closeModal();
        });
      }

      loadState();
      renderCalendar();
      renderTable("research");
      renderTable("admin");
      bindEvents();
    })();
  </script>
</body>
</html>
"""


def main() -> None:
    OUTPUT.write_text(HTML, encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
