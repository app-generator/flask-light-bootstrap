# Change Log

## [1.0.6] 2023-10-08
### Changes

- Update Dependencies
- Silent fallback to SQLite
- CI/CD for Render

## [1.0.5] 2022-06-11
### Changes

- Built with [Light Bootstrap Generator](https://appseed.us/generator/light-bootstrap-dashboard/)
 - Timestamp: `2022-06-11 12:19`

## [1.0.4] 2021-11-09
### Improvements

- Bump Codebase: [Flask Dashboard](https://github.com/app-generator/boilerplate-code-flask-dashboard) v2.0.0
  - Dependencies update (all packages) 
    - Flask==2.0.1 (latest stable version)
- Better Code formatting
- Improved Files organization
- Optimize imports
- Docker Scripts Update
- Gulp Tooling  (SASS Compilation)
- Fix **[ImportError: cannot import name 'TextField' from 'wtforms'](https://docs.appseed.us/content/how-to-fix/cannot-import-name-textfield-from-wtforms)**
  - Problem caused by `WTForms-3.0.0`
  - Fix: use **WTForms==2.3.3**

## [1.0.3] 2021-05-26
### Improvements

- Bump Codebase: [Flask Dashboard](https://github.com/app-generator/boilerplate-code-flask-dashboard) 1.0.6
- UI Kit: Light Bootstrap Dashboard - v2.0.1
- Bump UI: [Jinja Light Bootstrap](https://github.com/app-generator/jinja-light-bootstrap) 1.0.1

## [1.0.2] 2020-09-09
### Improvements

- 2020-09-09 - Update the codebase
    - Update boilerplate code
    - Update UI - v2.0.1

- 2020-08-20 - Added get_segment() helper that detects the current page
    - Updated files(s): app/home/routes.py

- 2020-06-22 - Guard Flask links with quotes
    - Sample href="{{ url_for('base_blueprint.login') }}"
    - Impacted files: login.html, register.html, sidebar.html

- 2020-06-22 - Added HEROKU support. Impacted files:
    - runtime.txt - Bump the Python version to 3.6.10
    - README added new section for HEROKU deployment

## [1.0.1] 2020-05-30
### Improvements & Bug Fixes

- Patch #Bug - Return a 403 Error for unauthorized access
- Update Licensing information
- Add CHANGELOG.md to track all changes

## [1.0.0] 2020-02-07
### Initial Release
