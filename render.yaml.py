services:
  - type: web
    name: bbg-birthday
    env: python
    buildCommand: ""
    startCommand: "gunicorn bbg_site:app"
