# Hero Banner Instructions

This guide will walk you through adding a dynamic, full-width hero banner to your Shopify store.

## 1. Recommended Banner Image

For the best results, use a high-quality, landscape-oriented image. We recommend this one, which fits your brand's aesthetic:

[**Download Basketball Image Here**](https://images.unsplash.com/photo-1612872087720-bb876e2e67d1?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8c3BvcnR8ZW58MHx8MHx8fDA%33D&fm=jpg&q=60&w=3000)

## 2. Liquid Code for a New Section

Here is the code for your new hero banner.

```liquid
{% comment %}
  This is the new and improved Hero Banner code.
  Key improvements:
  1. Banner Height setting: You can now easily change the banner's height in the theme editor to make it thinner or thicker.
  2. Overlap Fix: The banner will no longer cover your navigation buttons like "Catalog."
  3. Cleaner Code: Styles are separated for better performance and easier future edits.
  4. Interactive Button: The button now has a subtle hover effect that fits your red and black theme.
{% endcomment %}

{% schema %}
{
  "name": "Sportswear Hero Banner",
  "settings": [
    {
      "type": "image_picker",
      "id": "banner_image",
      "label": "Banner Image"
    },
    {
      "type": "range",
      "id": "banner_height",
      "min": 200,
      "max": 600,
      "step": 20,
      "unit": "px",
      "label": "Banner Height",
      "default": 340
    },
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Championship Kicks, Unbeatable Prices"
    },
    {
      "type": "textarea",
      "id": "subheading",
      "label": "Subheading",
      "default": "The ultimate superstore for every Dunk enthusiast."
    },
    {
      "type": "url",
      "id": "button_link",
      "label": "Button Link"
    },
    {
      "type": "text",
      "id": "button_text",
      "label": "Button Text",
      "default": "Explore the Collection"
    }
  ],
  "presets": [
    {
      "name": "Sportswear Hero Banner"
    }
  ]
}
{% endschema %}

<style>
  .hero-banner-wrapper {
    position: relative;
    text-align: center;
    color: white;
    /* This is the key fix to prevent the banner from covering your header/navigation */
    z-index: 0;
  }

  .hero-banner-wrapper .banner-image {
    display: block;
    width: 100%;
    object-fit: cover;
  }

  .hero-banner-wrapper .banner-text-overlay {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: rgba(0, 0, 0, 0.6);
    padding: 2rem;
    border-radius: 12px;
    width: 90%;
    max-width: 650px;
  }

  .hero-banner-wrapper .banner-heading {
    margin: 0 0 10px;
    font-size: 2.8em;
    font-weight: bold;
    line-height: 1.1;
  }

  .hero-banner-wrapper .banner-subheading {
    margin-bottom: 20px;
    font-size: 1.3em;
  }

  .hero-banner-wrapper .banner-button {
    padding: 14px 28px;
    background-color: #d30000; /* Bold red for your theme */
    border: none;
    border-radius: 5px;
    color: #fff;
    text-decoration: none;
    font-weight: bold;
    font-size: 1em;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
  }
  .hero-banner-wrapper .banner-button:hover {
    background-color: #a30000; /* Darker red on hover */
    transform: scale(1.05);
  }

  /* Responsive styles for smaller screens */
  @media (max-width: 768px) {
    .hero-banner-wrapper .banner-heading {
      font-size: 2em;
    }
    .hero-banner-wrapper .banner-subheading {
      font-size: 1em;
    }
    .hero-banner-wrapper .banner-button {
      padding: 12px 24px;
    }
  }
</style>

<div class="hero-banner-wrapper">
  {% if section.settings.banner_image != blank %}
    <img
      src="{{ section.settings.banner_image | image_url: width: 1600 }}"
      alt="{{ section.settings.banner_image.alt | escape }}"
      class="banner-image"
      style="height: {{ section.settings.banner_height }}px;"
    >
  {% else %}
    {% comment %} Show a placeholder when no image is selected in the editor {% endcomment %}
    <div class="shopify-section-placeholder" style="height: {{ section.settings.banner_height }}px; background-color: #222;">
      {{ 'lifestyle-1' | placeholder_svg_tag: 'placeholder-svg' }}
    </div>
  {% endif %}

  <div class="banner-text-overlay">
    {% if section.settings.heading != blank %}
      <h1 class="banner-heading">{{ section.settings.heading | escape }}</h1>
    {% endif %}
    {% if section.settings.subheading != blank %}
      <p class="banner-subheading">{{ section.settings.subheading | escape }}</p>
    {% endif %}
    {% if section.settings.button_link != blank and section.settings.button_text != blank %}
      <a href="{{ section.settings.button_link }}" class="banner-button">
        {{ section.settings.button_text | escape }}
      </a>
    {% endif %}
  </div>
</div>
```

## 3. How to Add the Banner to Your Theme

1.  **Go to Your Shopify Admin:**
    *   From your Shopify dashboard, go to **Online Store > Themes**.
2.  **Edit Your Theme Code:**
    *   Find the theme you want to edit, click the **...** button, and then click **Edit code**.
3.  **Create a New Section:**
    *   In the code editor, look for the **Sections** directory and click **Add a new section**.
    *   Name the new section `sportswear-hero-banner`.
    *   **Delete all the default code** that appears in the new file.
4.  **Paste the Code:**
    *   Copy the complete code from this file (above) and paste it into your new `sportswear-hero-banner.liquid` file.
    *   Click **Save**.
5.  **Add the Banner to a Page:**
    *   Go to the page where you want to add the banner (e.g., your homepage).
    *   Click **Add section** and search for "Sportswear Hero Banner."
    *   Upload the basketball image, customize the text, and enjoy your new banner!
