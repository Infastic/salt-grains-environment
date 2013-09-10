base:
  '*':
    - global

prd:
  'environment:prd':
    - match: grain
    - apps.salt-minion

pre:
  'environment:pre':
    - match: grain
    - apps.dsconfigad

dev:
  'environment:dev':
    - match: grain
    - apps.testapp
