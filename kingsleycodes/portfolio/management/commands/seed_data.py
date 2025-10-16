# portfolio/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from portfolio.models import Service, ServiceFAQ

SERVICES = [
    {
      'title': 'Mobile Development',
      'short': 'Android, Kotlin, Java, React Native apps.',
      'long': 'Native Android (Java/Kotlin) and cross-platform (React Native) mobile apps with payments and offline sync.',
      'faqs': [
        {'q': 'Do you build native apps?', 'a': 'Yes — Android using Java/Kotlin; I also work with React Native for cross-platform apps.'},
        {'q': 'Can you integrate payments?', 'a': 'Yes — REST API integrations, stripe, mobile money and crypto payments.'},
      ],
    },
    {
      'title': 'Web Development',
      'short': 'Django, React, Angular, Node, REST APIs.',
      'long': 'Full-stack web applications with Django backends and modern frontends (React/Next/Tailwind).',
      'faqs': [
        {'q': 'What stacks do you use?', 'a': 'Django REST, React, Angular, Node, Tailwind CSS, PostgreSQL.'},
        {'q': 'Can you deploy to production?', 'a': 'Yes — I deploy to AWS, PythonAnywhere, Render, and servers with CI/CD.'},
      ],
    },
    {
      'title': 'Desktop Development',
      'short': 'Java desktop apps, Python GUI tools.',
      'long': 'Desktop utilities and internal tools with Java & Python (Tkinter/ttkbootstrap).',
      'faqs': [
        {'q': 'Which platforms?', 'a': 'Primarily Windows and cross-platform Java-based apps.'},
      ],
    },
    {
      'title': 'DevOps & Cloud Engineering',
      'short': 'CI/CD, Docker, automation, server deployments.',
      'long': 'Automated deployments, Docker, monitoring, and scalable infrastructure design.',
      'faqs': [
        {'q': 'Do you manage cloud infra?', 'a': 'Yes—setup CI/CD, Docker containers, and monitor production systems.'},
      ],
    },
    {
      'title': 'Blockchain Engineering',
      'short': 'Solana, wallets, token integrations.',
      'long': 'Crypto wallets, Solana SPL tokens, secure transaction integrations and blockchain API work.',
      'faqs': [
        {'q': 'Which chains?', 'a': 'Solana (SPL) primarily, Ethereum (ETH) and Bitcoin (BTC) with wallet integrations and secure transaction design.'},
      ],
    },
    {
      'title': 'AI & Automation',
      'short': 'Automation pipelines and AI-assisted features.',
      'long': 'Automation with Celery + Redis, and AI integrations for data processing and alerts.',
      'faqs': [
        {'q': 'Do you build AI pipelines?', 'a': 'Yes — I integrate ML/AI services for automation and real-time alerts.'},
      ],
    },
    {
      'title': 'S.E.O & Digital Marketing',
      'short': 'SEO, performance, content strategy.',
      'long': 'On-page SEO improvements, performance optimization, and content-driven organic growth.',
      'faqs': [
        {'q': 'Can you improve page speed?', 'a': 'Yes — optimizations for server, assets, and frontend for better SEO.'},
      ],
    },
    {
      'title': 'Creative Studio Design',
      'short': 'UI/UX, branding, Canva designs, video editing.',
      'long': 'UI/UX, brand identity, marketing visuals and short-form videos (Reels/Shorts) using Canva and other tools.',
      'faqs': [
        {'q': 'What deliverables?', 'a': 'UI prototypes, branding packages, social media short videos and thumbnails.'},
      ],
    },
    {
      'title': 'Technical Writing',
      'short': 'Project reports, documentation & research writing.',
      'long': 'Technical reports, design docs, and user manuals written to professional standards.',
      'faqs': [
        {'q': 'Do you write project reports?', 'a': 'Yes — I produce detailed technical and business reports.'},
      ],
    },
]

class Command(BaseCommand):
    help = 'Seed initial services and FAQs'

    def handle(self, *args, **options):
        for idx, s in enumerate(SERVICES):
            service, created = Service.objects.get_or_create(
                title=s['title'],
                defaults={
                    'short_description': s['short'],
                    'long_description': s['long'],
                    'order': idx
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created service: {service.title}'))
            else:
                service.short_description = s['short']
                service.long_description = s['long']
                service.order = idx
                service.save()
                self.stdout.write(self.style.NOTICE(f'Updated service: {service.title}'))

            # add FAQs
            ServiceFAQ.objects.filter(service=service).delete()  # reset
            for fidx, faq in enumerate(s.get('faqs', [])):
                ServiceFAQ.objects.create(service=service, question=faq['q'], answer=faq['a'], order=fidx)
                self.stdout.write(self.style.SUCCESS(f'  added FAQ: {faq["q"]}'))

        self.stdout.write(self.style.SUCCESS('Seeding complete.'))
