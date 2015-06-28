from django.forms import ModelForm
from stokosm.models import Goal, Requirement, Project, Connection, Link
from admin import connection_creator, link_creator

class GoalForm(ModelForm):
	class Meta:
		model = Goal
		fields = ['name', 'description']

class RequirementForm(ModelForm):
	class Meta:
		model = Requirement
		fields = ['name', 'description']

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['name', 'description']

class GoalConnectionForm(ModelForm):
	def save(self, force_insert=False, force_update=False, commit=True, goal1=None):
		instance = super(GoalConnectionForm, self).save(commit=False)
		instance.goal1 = goal1
		if commit:
			connection_creator(instance)
		return instance
	class Meta:
		model = Connection
		fields = ['goal2', 'directed', 'direction', 'description']

class RequirementConnectionForm(ModelForm):
	def save(self, force_insert=False, force_update=False, commit=True, requirement1=None):
		instance = super(RequirementConnectionForm, self).save(commit=False)
		instance.requirement1 = requirement1
		if commit:
			connection_creator(instance)
		return instance
	class Meta:
		model = Connection
		fields = ['requirement2', 'directed', 'direction', 'description']

class ProjectConnectionForm(ModelForm):
	def save(self, force_insert=False, force_update=False, commit=True, project1=None):
		instance = super(ProjectConnectionForm, self).save(commit=False)
		instance.project1 = project1
		if commit:
			connection_creator(instance)
		return instance
	class Meta:
		model = Connection
		fields = ['project2', 'directed', 'direction', 'description']

class LinkForm(ModelForm):
	def save(self, context, force_insert=False, force_update=False, commit=True):
		instance = super(LinkForm, self).save(commit=False)
		for node in context:
			instance[node] = context[node]
		if commit:
			link_creator(instance)
		return instance
	class Meta:
		asbtract = True

class GoalLinkForm(LinkForm):
	class Meta:
		model = Link
		fields = ['goal', 'description']

class RequirementLinkForm(LinkForm):
	class Meta:
		model = Link
		fields = ['requirement', 'description']

class ProjectLinkForm(LinkForm):
	class Meta:
		model = Link
		fields = ['project', 'description']