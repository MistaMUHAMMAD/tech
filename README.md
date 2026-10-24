# Muhammad Musa — IT Support & Technical Operations

A static professional portfolio covering workplace technology, systems support, troubleshooting, user assistance and technical operations. Built with HTML, CSS and vanilla JavaScript. No framework, package installation, database, API key or build command is required to publish it on GitHub Pages.

## Pages and downloads

- `index.html`: profile, technical areas, work history, selected case studies, skills, training, education, CV and contact.
- `projects.html`: six anonymised real-work case studies and one TS Academy team training project.
- `samples.html`: fourteen labelled demonstration projects, with filters and downloads.
- `assets/Muhammad_Musa_IT_CV.pdf`: a public CV prepared from the supplied source CV, with unsupported scale/metrics removed.
- `assets/documents/IT_Support_Sample_Workbook.xlsx`: four editable sheets with fictional asset, ticket, learning-risk and vendor records.
- `assets/documents/IT_Support_Field_Guide.pdf`: printable sample checklists, templates and diagrams.
- `assets/documents/IT_Support_Portfolio_Samples.zip`: the complete sample toolkit.

Real-work case studies, the TS Academy team training project and fictional samples are labelled separately. Two supplied training certificates are linked under `assets/documents/certificates/`. The team repository is maintained under Tonylinks; it is not presented as an individual repository or sole-authored project. The site does not imply a software-engineering, advanced cloud, cybersecurity-programme or formal IT-risk role.

## Publish updates to your GitHub Pages site

This package is already configured for:

| Setting | Value |
|---|---|
| GitHub username | MistaMUHAMMAD |
| Repository | https://github.com/MistaMUHAMMAD/tech |
| Portfolio URL | https://mistamuhammad.github.io/tech/ |
| LinkedIn | https://www.linkedin.com/in/muhammad-musa-0a37081aa/ |
| Phone | +234 814 805 7035 |

Your `tech` repository is a project site. Keep its name as `tech` to retain the `/tech/` address.

1. Unzip the delivery package and open `github-pages-site`.
2. Upload the CONTENTS of that folder to `MistaMUHAMMAD/tech`, replacing the existing site files. Keep `index.html` at the repository root. Do not upload the outer delivery folder, `owner-guide` or the ZIP as the site.
3. Include `assets/`, `projects/`, `tools/`, the HTML/CSS/JavaScript files, favicon files, `site.webmanifest`, `site-config.json`, `sitemap.xml`, `robots.txt` and `.nojekyll`.
4. Commit with a message such as `Update portfolio contact details and project-site metadata`.
5. Keep **Settings → Pages → Deploy from a branch → main → /(root)**. There is no need to create a new repository or rename this one.
6. Wait for **pages build and deployment** in Actions to finish successfully, then open https://mistamuhammad.github.io/tech/.
7. Check the GitHub and LinkedIn links, the displayed international phone number and the CV download. Hard-refresh if the browser shows an older version.

The supplied files already contain the confirmed links and sharing metadata. Running Python is not required to upload or publish this update.

For later reconfiguration, run from the website folder:

```bash
python tools/configure.py --username MistaMUHAMMAD --site-url https://mistamuhammad.github.io/tech/
python tools/validate.py
```

On Windows, `py` can replace `python`. Internal page, asset and download links are relative, so they work under `/tech/`. Canonical links, Open Graph images, structured data and the sitemap use the full project-site URL. No `CNAME` is included because no custom domain has been configured.

## Preview locally

Open `index.html` in your browser for a simple preview. For clipboard behaviour and an HTTP-like test, open a terminal in this folder, run `python -m http.server 8000`, and visit `http://localhost:8000/`. Stop the server with Ctrl+C. This command is only for your own computer; GitHub Pages serves the static files directly.

## Replace the CV

1. Export the final approved CV as PDF.
2. Replace `assets/Muhammad_Musa_IT_CV.pdf` with that file, keeping the exact case and filename.
3. In `index.html`, find `cv-updated` and update the month/year. Update `cv_last_updated` in `site-config.json` as a record of the change.
4. Commit the PDF and text change together. Confirm that both CV buttons download the new document.

Never publish a CV containing private referee numbers, home addresses, confidential employer information or claims you cannot explain. The current public CV has been prepared with these boundaries in mind.

## Add your real photo

1. Put a real JPG, PNG or WebP photo in `assets/images/`, for example `muhammad-musa.jpg`. Use a Markdown-safe filename and a reasonably compressed image.
2. Run `python tools/configure.py --photo assets/images/muhammad-musa.jpg`.
3. Check the crop on desktop and phone. The `.profile-photo` rule in `styles.css` controls the crop through `object-fit` and `object-position`.

The current initials avatar is intentional. No portrait was generated. To add a photo manually, replace the initials-avatar inside `#profile-image` with an `img` using class `profile-photo`, the photo path and alt text `Muhammad Musa`.

## Update experience, skills or projects

- The work-history timeline is in `index.html`, within `#experience`. Each role uses `.timeline-item`. Keep exact formal titles and verified dates.
- Each homepage case card is a `.case-card` in `#projects`.
- Full case reports are articles in `projects.html`, each with an `id` matching its links. Keep Situation, My responsibility, What I investigated, Tools/technologies, Actions taken, Outcome and Skills demonstrated. State any unknown outcome plainly.
- Markdown copies of case studies are under `projects/`. If you update a case, update its HTML, card summary and Markdown copy together.
- Samples are under `projects/samples/`. Add a `.sample-card` in `samples.html` with an honest label such as Lab Project or Portfolio Sample. Use an existing `data-category` for filtering, or add a new filter button.
- Rebuild the downloadable sample ZIP after editing sample files. Include the sample workbook and PDF if their contents changed. Do not put the ZIP inside itself.
- Skills are grouped by use, support, exposure and learning in `index.html`. No progress bars imply an unmeasured score.
- Completed training and current learning are separate. Backend Development is completed (TS Academy, 10 August 2026). Keep the certificate PDFs and their links in sync. The technical-support certificate has no public date because its printed date and seal year need clarification. Do not convert project-stack tags into claims that every module was built by one person.

The Excel tables have 50 prepared data rows (rows 8–57). When extending them, extend the table, formula range and validation together. CSV copies contain values, not workbook formulas or styles. The ticket tracker measures calendar hours; it does not claim SLA or working-hours calculations. The risk register's fictional score is likelihood × impact, with no formal thresholds. Vendor examples use fictional NGN prices.

## Change contact details

Search the HTML files and `script.js` for the old email, phone or LinkedIn URL and replace every occurrence. Update the structured-data values in `tools/configure.py` if you use the configuration helper later. Edit `site-config.json` for the configured username/site URL, then rerun the helper when those settings change.

The phone is displayed as `+234 814 805 7035`; its clickable link uses `tel:+2348148057035`. Keep the display and link consistent.

### Contact form

The form opens a `mailto:` draft with the visitor's name, email and message. The visitor must send it from their email app. The site does not submit, store or send the message. If no mail app is configured, the direct email link is the fallback.

To connect Formspree later, create your own endpoint, replace the form action with that endpoint and set method to POST. Remove the current `contact-form` submit handler from `script.js`, keep the existing `name` attributes (name, email, body), and replace the explanatory copy. Test the endpoint and display a real result before claiming that a message was sent. Do not put API secrets in a static repository.

## Custom domain later

1. Register a domain you control and verify it in GitHub account settings using GitHub's current instructions.
2. In the repository's **Settings → Pages → Custom domain**, add the intended hostname before changing its DNS.
3. For a subdomain such as `www`, create a CNAME at your DNS provider pointing to your actual `username.github.io` host, without `https://` or a path. For an apex domain, follow the current GitHub A/ALIAS/ANAME instructions linked below.
4. Keep the root `CNAME` file GitHub creates for branch publishing. Do not add wildcard DNS records.
5. After GitHub validates DNS and issues a certificate, enable Enforce HTTPS.
6. Run `python tools/configure.py --site-url https://your-real-domain.example/` using your actual domain and commit the updated metadata. If also changing username, pass both flags in the same command.

DNS and certificate changes can take time. Use GitHub's current documentation for record values rather than copying an old address list.

## If changes do not appear

- Confirm the commit is on the published branch and the Pages source is **main / (root)**.
- Check the Pages deployment in Actions. Fix failed builds rather than repeatedly pushing identical files.
- Check that `index.html` is at the publishing root and that file case matches each link exactly.
- Open the exact expected URL. An account site and a project site have different paths.
- After a successful deployment, hard-refresh (Ctrl+F5 or Ctrl+Shift+R on Windows) and try a private window.
- In browser developer tools → Network, select Disable cache while developer tools remain open, then reload.
- CSS and JavaScript links use `?v=1`. After changing these files, increment the version in every HTML page when a stale cache persists.
- For an old CV download, temporarily add a new query version to the PDF links or inspect the deployed PDF directly in a private window.

## Favicon checks

The repository contains a root `favicon.ico`, SVG icon, 16×16 and 32×32 PNGs, 180×180 Apple touch icon, and 192×192/512×512 manifest icons. Every HTML page references the icon resources, including versioned links for browser caching.

1. Open `/favicon.ico` and `/assets/icons/favicon-32x32.png` on the deployed site. Confirm that each loads and shows MM.
2. Check browser developer tools → Network for 404s on the icon or manifest URLs.
3. Confirm the HTML still contains `rel="icon"`, `rel="apple-touch-icon"` and `rel="manifest"` tags.
4. After changing an icon, increment its `?v=` value in all HTML files and close/reopen the tab. Test a private window because favicon caches can outlast a regular refresh.
5. For an old home-screen icon, remove the saved shortcut and add it again after the new version is deployed.

## Accessibility and static behaviour

Semantic landmarks, labelled inputs, a skip link, visible keyboard focus, responsive navigation, reduced-motion support and print styles are included. Main content and links remain available without JavaScript. JavaScript adds the mobile menu, sample filters, email-copy control and email-draft helper. No third-party fonts, analytics, trackers or runtime libraries are loaded.

## Repository metadata

Description: Professional portfolio of Muhammad Musa, covering IT support, workplace systems, technical operations and downloadable support samples.

About: I support users, troubleshoot workplace technology and keep technical documentation and digital workflows organised. Based in Abuja, Nigeria.

Topics: `it-support`, `ict`, `technical-support`, `systems-support`, `technical-operations`, `helpdesk`, `network-support`, `microsoft-365`, `technical-documentation`, `portfolio`, `github-pages`.

## Folder structure

```text
github-pages-site/
  .gitignore
  .nojekyll
  404.html
  README.md
  assets/Muhammad_Musa_IT_CV.pdf
  assets/documents/IT_Support_Field_Guide.pdf
  assets/documents/IT_Support_Portfolio_Samples.zip
  assets/documents/IT_Support_Sample_Workbook.xlsx
  assets/documents/certificates/TS_Academy_Backend_Development_Certificate.pdf
  assets/documents/certificates/Technical_Support_Professional_Certificate.pdf
  assets/icons/android-chrome-192x192.png
  assets/icons/android-chrome-512x512.png
  assets/icons/apple-touch-icon.png
  assets/icons/favicon-16x16.png
  assets/icons/favicon-32x32.png
  assets/icons/favicon.svg
  assets/images/social-preview.png
  favicon.ico
  index.html
  projects/business-systems.md
  projects/cctv-storage.md
  projects/device-support.md
  projects/office-network.md
  projects/samples/01_IT_Asset_Register.csv
  projects/samples/02_Helpdesk_Ticket_Tracker.csv
  projects/samples/03_Onboarding_Offboarding_Checklist.md
  projects/samples/04_IT_Incident_Report_Template.md
  projects/samples/05_Preventive_Maintenance_Checklist.md
  projects/samples/06_Network_Documentation_Template.md
  projects/samples/07_Device_Troubleshooting_Decision_Tree.md
  projects/samples/07_Device_Troubleshooting_Decision_Tree.svg
  projects/samples/08_Backup_Verification_Checklist.md
  projects/samples/09_Basic_IT_Risk_Register.csv
  projects/samples/10_Microsoft_365_User_Support_Guide.md
  projects/samples/11_Windows_Support_Checklist.md
  projects/samples/12_Small_Office_Network_Diagram.svg
  projects/samples/13_Digital_Filing_Structure.md
  projects/samples/14_Vendor_Procurement_Comparison.csv
  projects/samples/README.md
  projects/ts-academy-hr-payroll.md
  projects/website-domain.md
  projects/workplace-support.md
  projects.html
  robots.txt
  samples.html
  script.js
  site-config.json
  site.webmanifest
  sitemap.xml
  styles.css
  tools/configure.py
  tools/validate.py
```

## Official references

Checked 24 October 2026:

- [Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [Configuring a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [Securing GitHub Pages with HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)
- [Microsoft Outlook connectivity support resources](https://learn.microsoft.com/en-us/troubleshoot/exchange/outlook-issues/office-365-troubleshooting-resources)
