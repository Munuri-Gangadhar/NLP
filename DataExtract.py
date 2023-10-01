import requests
from bs4 import BeautifulSoup
import os

def scrape_and_save_to_file(urls):
    for url in urls:
        # Send a request to the URL and get the HTML content
        response = requests.get(url).text
        data = BeautifulSoup(response, 'lxml')

        # Extract title and paragraph content
        title = data.find('title').text
        para = data.find('div', class_='td-post-content tagdiv-type').text

        # Create the desired file name
        file_name = url.split('/')
        desired_segment = '-'.join(file_name[3:])

        # Create the 'Data' directory if it doesn't exist
        if not os.path.exists('Data'):
            os.makedirs('Data')

        # Save the content to a text file
        with open(f'Data/{desired_segment}.txt', 'w') as f:
            f.write(f'''
                  {title}
                  {para}
                  ''')

# Example usage with multiple URLs




    
urls = [
    "https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-3-2/",
    "https://insights.blackcoffer.com/rise-of-e-health-and-its-impact-on-humans-by-the-year-2030/",
    "https://insights.blackcoffer.com/rise-of-e-health-and-its-imapct-on-humans-by-the-year-2030-2/",
    "https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-2/",
    "https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-2-2/",
    "https://insights.blackcoffer.com/rise-of-chatbots-and-its-impact-on-customer-support-by-the-year-2040/",
    "https://insights.blackcoffer.com/rise-of-e-health-and-its-imapct-on-humans-by-the-year-2030/",
    "https://insights.blackcoffer.com/how-does-marketing-influence-businesses-and-consumers/",
    "https://insights.blackcoffer.com/how-advertisement-increase-your-market-value/",
    "https://insights.blackcoffer.com/negative-effects-of-marketing-on-society/",
    "https://insights.blackcoffer.com/how-advertisement-marketing-affects-business/",
    "https://insights.blackcoffer.com/rising-it-cities-will-impact-the-economy-environment-infrastructure-and-city-life-by-the-year-2035/",
    "https://insights.blackcoffer.com/rise-of-ott-platform-and-its-impact-on-entertainment-industry-by-the-year-2030/",
    "https://insights.blackcoffer.com/rise-of-electric-vehicles-and-its-impact-on-livelihood-by-2040/",
    "https://insights.blackcoffer.com/rise-of-electric-vehicle-and-its-impact-on-livelihood-by-the-year-2040/",
    "https://insights.blackcoffer.com/oil-prices-by-the-year-2040-and-how-it-will-impact-the-world-economy/",
    "https://insights.blackcoffer.com/an-outlook-of-healthcare-by-the-year-2040-and-how-it-will-impact-human-lives/",
    "https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/",
    "https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/",
    "https://insights.blackcoffer.com/what-jobs-will-robots-take-from-humans-in-the-future/",
    "https://insights.blackcoffer.com/will-machine-replace-the-human-in-the-future-of-work/",
    "https://insights.blackcoffer.com/will-ai-replace-us-or-work-with-us/",
    "https://insights.blackcoffer.com/man-and-machines-together-machines-are-more-diligent-than-humans-blackcoffe/",
    "https://insights.blackcoffer.com/in-future-or-in-upcoming-years-humans-and-machines-are-going-to-work-together-in-every-field-of-work/",
    "https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/",
    "https://insights.blackcoffer.com/how-machine-learning-will-affect-your-business/",
    "https://insights.blackcoffer.com/deep-learning-impact-on-areas-of-e-learning/",
    "https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/",
    "https://insights.blackcoffer.com/how-machines-ai-automations-and-robo-human-are-effective-in-finance-and-banking/",
    "https://insights.blackcoffer.com/ai-human-robotics-machine-future-planet-blackcoffer-thinking-jobs-workplace/",
    "https://insights.blackcoffer.com/how-ai-will-change-the-world-blackcoffer/",
    "https://insights.blackcoffer.com/future-of-work-how-ai-has-entered-the-workplace/",
    "https://insights.blackcoffer.com/ai-tool-alexa-google-assistant-finance-banking-tool-future/",
    "https://insights.blackcoffer.com/ai-healthcare-revolution-ml-technology-algorithm-google-analytics-industrialrevolution/",
    "https://insights.blackcoffer.com/all-you-need-to-know-about-online-marketing/",
    "https://insights.blackcoffer.com/evolution-of-advertising-industry/",
    "https://insights.blackcoffer.com/how-data-analytics-can-help-your-business-respond-to-the-impact-of-covid-19/",
    "https://insights.blackcoffer.com/covid-19-environmental-impact-for-the-future/",
    "https://insights.blackcoffer.com/environmental-impact-of-the-covid-19-pandemic-lesson-for-the-future/",
    "https://insights.blackcoffer.com/how-data-analytics-and-ai-are-used-to-halt-the-covid-19-pandemic/",
    "https://insights.blackcoffer.com/difference-between-artificial-intelligence-machine-learning-statistics-and-data-mining/",
    "https://insights.blackcoffer.com/how-python-became-the-first-choice-for-data-science/",
    "https://insights.blackcoffer.com/how-google-fit-measure-heart-and-respiratory-rates-using-a-phone/",
    "https://insights.blackcoffer.com/what-is-the-future-of-mobile-apps/",
    "https://insights.blackcoffer.com/impact-of-ai-in-health-and-medicine/",
    "https://insights.blackcoffer.com/telemedicine-what-patients-like-and-dislike-about-it/",
    "https://insights.blackcoffer.com/how-we-forecast-future-technologies/",
    "https://insights.blackcoffer.com/can-robots-tackle-late-life-loneliness/",
    "https://insights.blackcoffer.com/embedding-care-robots-into-society-socio-technical-considerations/",
    "https://insights.blackcoffer.com/management-challenges-for-future-digitalization-of-healthcare-services/",
    "https://insights.blackcoffer.com/are-we-any-closer-to-preventing-a-nuclear-holocaust/",
    "https://insights.blackcoffer.com/will-technology-eliminate-the-need-for-animal-testing-in-drug-development/",
    "https://insights.blackcoffer.com/will-we-ever-understand-the-nature-of-consciousness/",
    "https://insights.blackcoffer.com/will-we-ever-colonize-outer-space/",
    "https://insights.blackcoffer.com/what-is-the-chance-homo-sapiens-will-survive-for-the-next-500-years/",
    "https://insights.blackcoffer.com/why-does-your-business-need-a-chatbot/",
    "https://insights.blackcoffer.com/how-you-lead-a-project-or-a-team-without-any-technical-expertise/",
    "https://insights.blackcoffer.com/can-you-be-great-leader-without-technical-expertise/",
    "https://insights.blackcoffer.com/how-does-artificial-intelligence-affect-the-environment/",
    "https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes-2/",
    "https://insights.blackcoffer.com/is-perfection-the-greatest-enemy-of-productivity/",
    "https://insights.blackcoffer.com/global-financial-crisis-2008-causes-effects-and-its-solution/",
    "https://insights.blackcoffer.com/gender-diversity-and-equality-in-the-tech-industry/",
    "https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes/",
    "https://insights.blackcoffer.com/how-small-business-can-survive-the-coronavirus-crisis/",
    "https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors-and-food-stalls/",
    "https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors/",
    "https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-tourism-aviation-industries/",
    "https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-sports-events-around-the-world/",
    "https://insights.blackcoffer.com/changing-landscape-and-emerging-trends-in-the-indian-it-ites-industry/",
    "https://insights.blackcoffer.com/online-gaming-adolescent-online-gaming-effects-demotivated-depression-musculoskeletal-and-psychosomatic-symptoms/",
    "https://insights.blackcoffer.com/human-rights-outlook/",
    "https://insights.blackcoffer.com/how-voice-search-makes-your-business-a-successful-business/",
    "https://insights.blackcoffer.com/how-the-covid-19-crisis-is-redefining-jobs-and-services/",
    "https://insights.blackcoffer.com/how-to-increase-social-media-engagement-for-marketers/",
    "https://insights.blackcoffer.com/impacts-of-covid-19-on-streets-sides-food-stalls/",
    "https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets-2/",
    "https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-5/",
    "https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-4/",
    "https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-2/",
    "https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-3/",
    "https://insights.blackcoffer.com/travel-and-tourism-outlook/",
    "https://insights.blackcoffer.com/gaming-disorder-and-effects-of-gaming-on-health/",
    "https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation/",
    "https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation-2/",
    "https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-office-space-and-co-working-industries/",
    "https://insights.blackcoffer.com/contribution-of-handicrafts-visual-arts-literature-in-the-indian-economy/",
    "https://insights.blackcoffer.com/how-covid-19-is-impacting-payment-preferences/",
    "https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-2/",
    "https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis/",
    "https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding/",
    "https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-2/",
    "https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-3/",
    "https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-3/",
    "https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work/",
    "https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding-2/",
    "https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-4/",
    "https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-2/",
    "https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-3/",
    "https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-4/",
    "https://insights.blackcoffer.com/why-scams-like-nirav-modi-happen-with-indian-banks/",
    "https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy/",
    "https://insights.blackcoffer.com/impact-of-covid-19coronavirus-on-the-indian-economy-2/",
    "https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy-2/",
    "https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy-3/",
    "https://insights.blackcoffer.com/should-celebrities-be-allowed-to-join-politics/",
    "https://insights.blackcoffer.com/how-prepared-is-india-to-tackle-a-possible-covid-19-outbreak/",
    "https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work/",
    "https://insights.blackcoffer.com/controversy-as-a-marketing-strategy/",
    "https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry/",
    "https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets/",
    "https://insights.blackcoffer.com/what-are-the-key-policies-that-will-mitigate-the-impacts-of-covid-19-on-the-world-of-work/",
    "https://insights.blackcoffer.com/marketing-drives-results-with-a-focus-on-problems/",
    "https://insights.blackcoffer.com/continued-demand-for-sustainability/"
]

scrape_and_save_to_file(urls)