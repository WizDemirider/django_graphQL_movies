import graphene
import movies.moviesApp.schema

class Query(movies.moviesApp.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(movies.moviesApp.schema.Mutation, graphene.ObjectType):  
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
