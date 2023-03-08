# == Schema Information
#
# Table name: projects
#
#  id               :integer          not null, primary key
#  completionstatus :boolean
#  text             :string
#  title            :string
#  created_at       :datetime         not null
#  updated_at       :datetime         not null
#  user_id          :integer
#
class Project < ApplicationRecord
  belongs_to(:owner, { :required => true, :class_name => "User", :foreign_key => "user_id" })
end
