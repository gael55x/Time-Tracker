from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login, logout
from .models import Project, TimeEntry, TaskDescription
from .serializer import ProjectSerializer, TimeEntrySerializer, TaskDescriptionSerializer, UserRegisterSerializer, UserLoginSerializer, UserSerializer
from .validations import custom_validation, validate_email, validate_password

class UserRegister(APIView):
    """
    API view for user registration.
    
    Request Args:
        - request.data: User registration data including username, email, and password.

    Returns:
        - Response: HTTP response object containing user registration data if successful, or an error message if failed.
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    """
    API view for user login.
    
    Request Args:
        - request.data: User login data including email and password.

    Returns:
        - Response: HTTP response object containing a success message and user data if login is successful,
                    or an error message if login fails.
    """
    permission_classes = (AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
    """
    API view for user logout.

    Returns:
        - Response: HTTP response object containing a success message if logout is successful,
                    or an error message if logout fails.
    """
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    """
    API view for user details.
    
    Returns:
        - Response: HTTP response object containing user details if the user is authenticated,
                    or an error message if the user is not authenticated.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    
# Get, update, or delete a specific project
class ProjectDetailAPIView(APIView):
    """API view for managing a specific project."""

    serializer_class = ProjectSerializer

    def get(self, request, pk):
        """Retrieve a specific project.
        
        Args:
            request: HTTP request object.
            pk: Project ID to retrieve a specific project.

        Returns:
            Response: HTTP response object containing the project data.
        """
        project = Project.objects.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update a specific project.
        
        Args:
            request: HTTP request object.
            pk: Project ID to update.

        Returns:
            Response: HTTP response object with the updated project data.
        """
        project = Project.objects.get(pk=pk)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a specific project.
        
        Args:
            request: HTTP request object.
            pk: Project ID to delete.

        Returns:
            Response: HTTP response object indicating success or failure.
        """
        project = Project.objects.get(pk=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get all projects or create a new project
class ProjectListAPIView(APIView):
    """API view for managing all projects."""

    serializer_class = ProjectSerializer

    def get(self, request):
        """Retrieve a list of all projects.
        
        Args:
            request: HTTP request object.

        Returns:
            Response: HTTP response object containing a list of projects.
        """
        projects = Project.objects.all()
        output = [{"id": project.id, "name": project.name} for project in projects]
        return Response(output)

    def post(self, request):
        """Create a new project.
        
        Args:
            request: HTTP request object.

        Returns:
            Response: HTTP response object with the created project data.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Get all time entries for all users or create a new time entry
class TimeEntryListAPIView(APIView):
    """API view for managing all time entries for all users."""

    serializer_class = TimeEntrySerializer

    def get(self, request):
        """Retrieve a list of all time entries for all users.

        Args:
            request: HTTP request object.

        Returns:
            Response: HTTP response object containing a list of time entries for all users.
        """
        time_entries = TimeEntry.objects.all()
        serializer = self.serializer_class(time_entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new time entry.

        Args:
            request: HTTP request object.

        Returns:
            Response: HTTP response object with the created time entry data.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Get, update, post or delete a specific time entry for a specific user
class TimeEntryDetailAPIView(APIView):
    """API view for managing a specific time entry."""

    serializer_class = TimeEntrySerializer

    def get(self, request, pk):
        """Retrieve a specific time entry.
        
        Args:
            request: HTTP request object.
            pk: Time Entry ID to retrieve a specific time entry.

        Returns:
            Response: HTTP response object containing the time entry data.
        """
        time_entry = TimeEntry.objects.get(pk=pk)
        serializer = self.serializer_class(time_entry)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update a specific time entry.
        
        Args:
            request: HTTP request object.
            pk: Time Entry ID to update.

        Returns:
            Response: HTTP response object with the updated time entry data.
        """
        time_entry = TimeEntry.objects.get(pk=pk)
        serializer = self.serializer_class(time_entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete a specific time entry.
        
        Args:
            request: HTTP request object.
            pk: Time Entry ID to delete.

        Returns:
            Response: HTTP response object indicating success or failure.
        """
        time_entry = TimeEntry.objects.get(pk=pk)
        time_entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TaskDescriptionListAPIView(APIView):
    """API view for managing a list of task descriptions."""

    serializer_class = TaskDescriptionSerializer

    def get_queryset(self):
        return TaskDescription.objects.all()

    def get(self, request):
        """Retrieve a list of all task descriptions.
        
        Args:
            request: HTTP request object.

        Returns:
            Response: HTTP response object containing a list of task descriptions.
        """
        task_descriptions = self.get_queryset()
        serializer = self.serializer_class(task_descriptions, many=True)
        return Response(serializer.data)

    # POST REQUEST DOESN'T WORK WITHOUT A USER ID IN THE FIRST PLACE
    def post(self, request):
        """Create a new task description.
        
        Args:
            request: HTTP request object.

        Returns:
            Response: HTTP response object with the created task description data.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDescriptionDetailAPIView(APIView):
    """API view for managing a single task description."""

    serializer_class = TaskDescriptionSerializer

    def get_object(self, pk):
        try:
            return TaskDescription.objects.get(pk=pk)
        except TaskDescription.DoesNotExist:
            return None

    def get(self, request, pk):
        """Retrieve a single task description by ID.
        
        Args:
            request: HTTP request object.
            pk: Primary key of the task description to retrieve.

        Returns:
            Response: HTTP response object containing the task description data.
        """
        task_description = self.get_object(pk)
        if not task_description:
            return Response({"error": "Task description not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(task_description)
        return Response(serializer.data)

    def delete(self, request, pk):
        """Delete a task description.
        
        Args:
            request: HTTP request object.
            pk: Task Description ID to delete.

        Returns:
            Response: HTTP response object indicating success or failure.
        """
        task_description = self.get_object(pk)
        if not task_description:
            return Response({"error": "Task description not found"}, status=status.HTTP_404_NOT_FOUND)
        
        task_description.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)