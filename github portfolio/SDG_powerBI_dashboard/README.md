# Block A - Business Understanding

Block A focuses on the first stage of the *__CRISP-DM__* process, known as *__Business Understanding__*. This phase entails acquiring a deep understanding of the business context and requirements.

During this phase, you will acquire the skills necessary to formulate a research question that can be addressed through data analysis. You will learn how to find, and collect appropriate data from relevant sources, explore and analyze the collected data, and visualize your findings effectively using the programming language Python and the dashboarding tool Power BI. By doing so, you will be able to propose a solution to your research question, substantiated by sound arguments derived from your analysis. Finally, you will gain proficiency in presenting your findings to the client in a clear and concise manner.

## Creative Brief

The Sustainable Development Goals (SDGs) were established by the United Nations in 2015 to guide countries in achieving a sustainable future. These 17 global objectives encompass a wide range of areas, including poverty eradication, education, gender equality, economic growth, climate action, and environmental protection.

The *__SDG Hub@BUas__*, referred to as the client, has reached out to you as an aspiring - *__data professional__* - to apply your expertise in providing data-driven solutions. In particular, they require your assistance in monitoring and assessing the advancements made towards the SDGs on a global and/or country-specific scale. 


The objective is to *__develop an interactive dashboard utilizing your newly acquired skills in data analytics and visualization__*. The dashboard will provide valuable insights to policymakers, researchers, and activists, enabling them to make informed decisions and take targeted actions towards the SDGs. Moreover, it will serve as a tool to raise awareness among the general public, inspiring collective efforts towards creating a more sustainable and equitable world.
------------

# Air Pollution and SDG Goals Dashboard

## Overview

This Power BI dashboard analyzes the relationship between fine particulate matter (PM 2.5) levels in urban environments and their contribution to achieving Sustainable Development Goals, specifically:
- **SDG 3.9.1**: Substantially reduce deaths and illnesses from air pollution
- **SDG 11.6.2**: Reduce the adverse environmental impact of cities, including air quality

The dashboard visualizes global air pollution data from 1990-2020, examining deaths caused by various types of air pollution across different countries and tracking trends over three decades.

---

## Dashboard Structure

### 1. Cover Page
**Purpose**: Introduction and context setting

**Components**:
- **SDG Icons**: Displays SDG 3 (Good Health and Well-being) and SDG 11 (Sustainable Cities and Communities)
- **Research Question**: Frames the dashboard's focus on PM 2.5 monitoring and SDG achievement
- **Visual Illustration**: Conceptual representation of urban air pollution
- **QR Code**: Provides quick access to additional resources or the dashboard itself

**Benefit**: Sets clear expectations and establishes the policy/research context for stakeholders.

---

### 2. Map View - Global Air Pollution Overview
**Purpose**: Provide a geographic overview of air pollution deaths worldwide

**Components**:

**Key Statistics Panel** (Top):
- Sum of Deaths: 197.66M total deaths (1990-2019)
- Maximum Deaths: 1.92M (single country peak)
- Minimum Deaths: 0.19 (lowest recorded)
- Standard Deviation: 164.49K (showing high variability)
- Average Deaths: 31.68K per country
- Median Deaths: 4.12K (typical country impact)

**Interactive World Map**:
- Purple bubble markers sized by death rates
- Geographic clustering reveals regional pollution hotspots
- Largest concentrations visible in Asia, Africa, and parts of Europe

**Filter Panel** (Left sidebar):
- Country selection list (alphabetical)
- Enables focused analysis on specific nations

**Year Slider** (Bottom):
- Range: 1990-2019
- Allows temporal analysis of pollution trends

**Benefits**:
- Identifies global hotspots requiring immediate intervention
- Enables comparison between regions and countries
- Supports evidence-based policy prioritization
- Reveals geographic patterns in air pollution mortality

---

### 3. Different Types of Air Pollution (Country Detail View)
**Purpose**: Break down pollution sources and their mortality impact for individual countries

**Components**:

**Pie Chart - Percentage Distribution**:
- Smoking (dark teal)
- Secondhand smoke (light teal)
- Ambient particulate matter pollution (pink)
- Household air pollution from solid fuels (purple)
- Shows relative contribution of each pollution type to total deaths

**Time Series Charts** (4 separate graphs):
1. Deaths by household air pollution from solid fuels (1990-2020)
2. Deaths by smoking (1990-2020)
3. Deaths by secondhand smoke (1990-2020)
4. Deaths by ambient particulate matter pollution (1990-2020)

**Country Examples Shown**:
- **Pakistan**: Shows declining household pollution but rising ambient PM2.5 deaths
- **South Africa**: Displays different pattern with significant smoking-related mortality

**Benefits**:
- Identifies primary pollution sources per country
- Tracks effectiveness of interventions over time
- Reveals shifting pollution patterns (e.g., transition from household to ambient pollution)
- Enables targeted policy recommendations based on dominant pollution types
- Helps allocate resources to most impactful interventions

---

### 4. Countries Comparison (Developed vs. Developing)
**Purpose**: Analyze disparities between developed and developing nations

**Components**:

**Correlation Analysis** (Top Left):
- Scatter plot showing PM2.5 exposure vs. deaths
- Linear regression line
- Correlation coefficient: 0.70 (strong positive relationship)
- Compares 6 countries: China, Egypt, Morocco (developing) vs. Netherlands, Norway, United States (developed)

**PM2.5 Exposure Pie Chart** (Top Right):
- China: 30.61%
- Egypt: 38.76%
- Morocco: 15.2%
- Netherlands: 7%
- Norway: 4.01%
- United States: Not prominently shown
- Demonstrates disproportionate exposure in developing nations

**Stacked Bar Chart** (Bottom Left):
- Compares total death counts across pollution types
- Color-coded by pollution source
- Shows China has dramatically higher mortality burden
- Reveals different pollution profiles between country groups

**Multi-Line Trend Chart** (Bottom Right):
- Deaths from air pollution by year (1990-2020)
- Separate lines for each country
- China shows highest but slightly declining trend
- Developed countries show consistently low, stable rates
- Developing countries show varied trajectories

**Year Slider**:
- Enables temporal filtering across all visualizations

**Benefits**:
- Quantifies inequality in pollution burden
- Validates PM2.5 as reliable mortality predictor (0.70 correlation)
- Shows development-pollution relationship
- Highlights success of developed nations' air quality policies
- Identifies countries needing urgent intervention
- Supports arguments for technology transfer and capacity building

---

## Dashboard Relevance to SDG Goals

### SDG 3.9.1 (Substantially reduce deaths from air pollution)
**How the dashboard supports this goal**:
- Tracks mortality rates over 30 years, measuring progress toward reduction targets
- Identifies high-burden countries requiring immediate action
- Breaks down pollution sources to enable targeted health interventions
- Quantifies the scale of the problem (197.66M deaths 1990-2019)

### SDG 11.6.2 (Reduce adverse environmental impact of cities)
**How the dashboard supports this goal**:
- Focuses specifically on PM 2.5, the key urban air quality indicator
- Maps urban pollution hotspots for city-level planning
- Tracks ambient particulate matter trends separately from other pollution types
- Enables cities to benchmark against similar contexts

---

## Key Insights Enabled by This Dashboard

1. **Scale of Impact**: Quantifies the massive public health burden (197M+ deaths)
2. **Geographic Disparities**: Reveals developing nations bear disproportionate burden
3. **Pollution Transitions**: Tracks shift from household to ambient pollution in developing countries
4. **Policy Effectiveness**: Shows declining trends in countries with strong air quality regulations
5. **Source Attribution**: Identifies which pollution types to prioritize per country
6. **Temporal Trends**: Reveals whether countries are moving toward or away from SDG targets

---

## Use Cases

**For Policymakers**:
- Prioritize air quality interventions based on mortality burden
- Allocate resources to most impactful pollution sources
- Benchmark progress against similar countries
- Justify investments in clean energy and pollution control

**For Researchers**:
- Analyze correlation between development and pollution
- Study effectiveness of different intervention types
- Identify research gaps in high-burden, low-data countries

**For International Organizations**:
- Identify countries needing technical assistance
- Track SDG progress globally and regionally
- Support evidence-based advocacy and funding decisions

**For Public Health Officials**:
- Quantify disease burden attributable to air pollution
- Design targeted health communication campaigns
- Plan healthcare infrastructure for pollution-related illnesses

---

## Technical Features

- **Interactive Filtering**: Country and year selection across all pages
- **Multiple Visualization Types**: Maps, time series, pie charts, scatter plots, bar charts
- **Coordinated Views**: Filters apply across all dashboard pages
- **Statistical Summaries**: Key metrics for quick assessment
- **Temporal Analysis**: 30-year trend tracking
- **Comparative Analysis**: Country grouping and benchmarking

---

## Data Coverage

- **Geographic**: Global coverage with country-level detail
- **Temporal**: 1990-2020 (30 years)
- **Pollution Types**: Household solid fuel, smoking, secondhand smoke, ambient PM2.5
- **Metrics**: Death counts, correlation coefficients, percentage distributions

---

## Conclusion

This dashboard serves as a comprehensive tool for monitoring progress toward SDG 3.9.1 and 11.6.2 by providing actionable insights into air pollution mortality patterns. It enables data-driven decision-making for reducing the global burden of air pollution and achieving sustainable, healthy cities.