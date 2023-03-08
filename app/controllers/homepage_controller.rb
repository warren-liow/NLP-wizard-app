class HomepageController < ApplicationController
  def index
    render({ :template => "homepage/index.html.erb" })
  end

  def projects_page
    user = User.where(:id => session[:user_id]).first
    @username = user.first_name
    @projects = Project.where(:user_id => session[:user_id])
    @ongoing_projects = @projects.where(:completionstatus => false).order({ :updated_at => :desc })
    @completed_projects = @projects.where(:completionstatus => true).order({ :updated_at => :desc })
    render({ :template => "homepage/signed_in.html.erb" })
  end
end
