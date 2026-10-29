# Visuals for Substack Blogs

Welcome to the **Visuals for Substack Blogs** repository! This project serves as a centralized hub for all the interactive, sleek, and high-quality HTML widgets and data visualizations embedded within my Substack articles. 

Instead of relying on static images, these widgets leverage modern web technologies to provide readers with interactive calculators, dynamic diagrams, and animated UI teardowns directly within the reading experience.

---

## 📂 Project Structure

The repository is organized by blog post / topic, with each folder containing the specific HTML visual widgets for that article.

### 1. `AI-Pricing-Problem/`
Visuals exploring the unit economics, strategic friction points, and infrastructure costs of AI-native businesses.
* **`interactive_simulator_widget.html` / `simulator.html`**: An interactive AI Gross Margin Simulator that calculates API burn rates against subscription tiers.
* **`pricing_trilemma_visual.html` / `trilemma.html`**: A highly interactive, drag-to-balance triangular radar showing the tension between Adoption, Margins, and Retention.
* **`ai_product_archetypes_visual.html`**: Mapping of different AI application architectures.
* **`semantic_routing_visual.html`**: Diagram explaining LLM router logic.
* **`hosting/`**: Firebase deployment configuration for the unified live web app.

### 2. `Google-Photos-Teardown/`
A deep-dive product management teardown of Google Photos.
* **`metric_tree.html` / `product_metrics.html`**: Visualizations of the L1 and North Star metrics for the product.
* **`persona_cards.html`**: Beautifully styled profiles of the target user segments.
* **`user_journey.html` / `upgrade_funnel.html`**: Step-by-step visualizations of the user experience and monetization funnels.
* **`camera_evolution_timeline.html`**: Interactive historical timelines.

### 3. `Roblox-Teardown/`
A concise, player-focused product teardown following the Google Photos section structure.
* **`v1/`**: Reconstructed archive of the earlier card-based visual direction, with source HTML/CSS and its own PNG exports. Recreated from the conversation, not an exact backup of the overwritten files.
* **`v2/article.md`**: Revised article with the author's group horror-game introduction, personas and JTBD, journey, retention, monetization, proposed North Star/L1/L2 metrics, guardrails, opportunities, and a concept evaluation.
* **`v2/visuals.html` / `visuals.css` / `visuals.js`**: Nine bespoke, responsive visual essays: a 100-person crowd, original block characters, a walkable horror corridor, a discovery maze, a return railway, a monetization balance, a North Star constellation, an opportunity quest board, and a fictional mobile concept. Detailed definitions and experiment notes stay outside the artwork.
* **`v2/assets/`**: Nine original PNG panel exports embedded in the article. With Python Playwright and its Chromium available, run `python3 Roblox-Teardown/v2/export_visuals.py` to check and re-export; use `--check-only` for checks without changing images, or `--pdf /absolute/path/to/panels.pdf` for a nine-page print export. The script does not install dependencies.
* **`v2/media-sources.json`**: Verified original uploads from Roblox and Roblox Creators. Two click-to-load official YouTube players provide a promotional trailer and a recommendation-system explainer. No player contacts YouTube before the reader clicks; original-source links remain available. Public availability is **not** public-domain status: footage is not downloaded, clipped, or re-hosted.
* Facts link to primary sources and use a dated Q2 2026 business snapshot. Interface drawings are explicitly labeled schematics or concepts, not actual screenshots. Opportunities are hypotheses, not validated findings; RICE scores remain uncomputed without evidence.
* Open a version's `visuals.html` locally or serve the repository with `python3 -m http.server 8000` and visit `/Roblox-Teardown/v2/visuals.html`. Each panel has its own anchor; **Print field guide** exports the nine original panels, excluding live players. Use original video links in Substack and verify embed support rather than assuming iframe support.

---

## 🛠️ Technology Stack
These visualizations are built to be lightweight, incredibly fast, and easy to embed without heavy dependencies:
* **HTML5 & Vanilla JavaScript**: For flawless logic and DOM manipulation without framework overhead.
* **Tailwind CSS**: For sleek, rapid, and modern styling (glassmorphism, meshes, gradients).
* **Lucide Icons**: Clean, consistent SVG iconography.

---

## 🚀 Live Deployment

The visuals from the **AI Pricing Problem** article have been bundled into a unified Firebase Hosting web app. 

You can view the live interactive hub here:
👉 **[ai-pricing-strategy-visuals.web.app](https://ai-pricing-strategy-visuals.web.app)**

### Deployment Guide (Firebase)
To deploy updates to the live site:
1. Ensure you have the Firebase CLI installed: `npm install -g firebase-tools`
2. Navigate to the hosting directory: `cd AI-Pricing-Problem/hosting`
3. Run the deployment command: `firebase deploy --only hosting`

---

## 📝 Embedding in Substack
Because Substack has strict iframe and script security policies, these interactive visuals are often deployed via Firebase and then hyperlinked, or adapted into high-quality GIFs/WebMs for direct embedding depending on the platform's current support for rich interactive embeds. 
