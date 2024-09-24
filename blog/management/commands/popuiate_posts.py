from typing import Any
from blog.models import post
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "this commands inserts post data"
    
    def handle(self, *args: Any, **options: Any) :
         titles =[

        "Unlocking the Secrets of Mindfulness: A Beginner's Guide"
        "10 Budget-Friendly Travel Destinations You Can't Miss"
        "The Ultimate Guide to Sustainable Living in 2024"
        "How to Build a Morning Routine That Sticks"
        "The Future of Remote Work: Trends to Watch"
        "5 Simple Recipes for Healthy Weeknight Dinners"
        "The Power of Journaling: Transform Your Life One Page at a Time"
        "Top 10 Books to Inspire Your Creativity"
        "Navigating the World of Plant-Based Diets: Tips and Tricks"
        "Essential Tech Gadgets for Every Home Office"
        
        ]

         content =[
            "Define mindfulness and its significance, explore various mindfulness techniques (such as breathing exercises, body scans, and mindful walking), discuss daily mindfulness practices for incorporation into routines, provide resources like apps, books, and online courses, and share personal anecdotes or testimonials on the benefits of mindfulness"
            "Highlight 10 budget-friendly travel destinations, including key attractions and activities in each location, provide budget tips for accommodations and dining, share local attractions that offer free or low-cost experiences, and offer travel hacks for saving money on flights and transportation."
            "Define sustainable living and its importance, explore practical steps for reducing waste and conserving resources, discuss eco-friendly alternatives for daily products, highlight community initiatives and organizations to support, provide tips for sustainable transportation and energy use, and share resources for further learning, including books, documentaries, and online courses."
            "Discuss the importance of a morning routine for productivity and well-being, share key elements of an effective routine (like wake-up time, hydration, exercise, and mindfulness), provide tips for gradually implementing new habits, suggest tools and apps for tracking progress, and include examples of successful morning routines from various individuals."
            "Explore emerging trends in remote work, such as hybrid work models and increased flexibility, discuss technological advancements facilitating remote collaboration (like virtual reality and AI tools), analyze the impact of remote work on company culture and employee well-being, highlight the importance of work-life balance, and provide predictions for the future landscape of remote employment and its challenges."
            "Provide 5 quick and nutritious dinner recipes, including ingredient lists, preparation steps, and cooking times, highlight health benefits of each dish, suggest variations or substitutions for dietary preferences, and include tips for meal prep and storage to save time during the week."
            "Discuss the benefits of journaling for mental health, self-reflection, and creativity, explore different journaling techniques (such as gratitude journaling, bullet journaling, and free writing), provide prompts to get started, share tips for establishing a consistent journaling habit, and highlight resources like apps and books that enhance the journaling experience."
            "List 10 influential books that spark creativity, provide brief summaries and key takeaways for each book, discuss the authors' backgrounds and their contributions to creative thinking, include quotes or concepts from the books that resonate, and suggest ways to apply insights from these readings to everyday creative practices"
            "Define plant-based diets and their health benefits, share tips for transitioning to a plant-based lifestyle, provide meal planning ideas and easy recipes, discuss essential nutrients to focus on (like protein, iron, and B12), highlight common misconceptions, and recommend resources such as cookbooks, blogs, and online communities for support."
            "List must-have tech gadgets for a home office setup, including items like ergonomic keyboards, high-quality webcams, and noise-canceling headphones, provide features and benefits of each gadget, discuss how these tools enhance productivity and comfort, suggest budget-friendly alternatives, and include tips for integrating technology effectively into your workspace."

            
            ]

         img_urls =[
            "https://picsum.photos/id/1/800/400"
            "https://picsum.photos/id/2/800/400"
            "https://picsum.photos/id/3/800/400"
            "https://picsum.photos/id/4/800/400"
            "https://picsum.photos/id/5/800/400"
            "https://picsum.photos/id/6/800/400"
            "https://picsum.photos/id/7/800/400"
            "https://picsum.photos/id/8/800/400"
            "https://picsum.photos/id/9/800/400"
            "https://picsum.photos/id/10/800/400"
            ]

         for title,content,img_urls in zip(titles,content,img_urls):
            post.objects.create(title=title, content=content, img_urls=img_urls)}
            
        self.stdout.write(self.style.SUCCESS("Completed inserting data!"))
    