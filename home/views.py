from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['technologies'] = [
            {'name': 'Python', 'img': 'python.png'},
            {'name': 'Flask', 'img': 'flask.png'},
            {'name': 'Django', 'img': 'django.png'},
            {'name': 'Java', 'img': 'java.png'},
            {'name': 'Spring Boot', 'img': 'spring_boot.png'},
            {'name': 'TypeScript', 'img': 'typescript.png'},
            {'name': 'Next.js', 'img': 'nextjs.png'},
            {'name': 'Kubernetes', 'img': 'kubernetes.png'},
            {'name': 'Microservices', 'img': 'microservices.png'},
            {'name': 'Docker', 'img': 'docker.png'},
            {'name': 'Helm', 'img': 'helm.png'},
            {'name': 'MS SQL Server', 'img': 'mssql.png'},
            {'name': 'PostgreSQL', 'img': 'postgresql.png'},
            {'name': 'Couchbase', 'img': 'couchbase.png'},
            {'name': 'Distributed Hazelcast', 'img': 'hazelcast.png'},
            {'name': 'Redis', 'img': 'redis.png'},
            {'name': 'BigQuery', 'img': 'bigquery.png'},
            {'name': 'GitHub CI/CD', 'img': 'github_cicd.png'},
            {'name': 'Jenkins', 'img': 'jenkins.png'},
            {'name': 'SonarQube', 'img': 'sonarqube.png'},
            {'name': 'Swagger', 'img': 'swagger.png'},
            {'name': 'Postman', 'img': 'postman.png'},
            {'name': 'Pydantic', 'img': 'pydantic.png'},
            {'name': 'REST APIs', 'img': 'restapi.png'},
            {'name': 'Agile', 'img': 'agile.png'},
            {'name': 'Jira', 'img': 'jira.png'},
            {'name': 'Confluence', 'img': 'confluence.png'},
        ]

        return context
