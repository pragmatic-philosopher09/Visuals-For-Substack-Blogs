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
