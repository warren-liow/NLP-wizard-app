class CreateProjects < ActiveRecord::Migration[6.0]
  def change
    create_table :projects do |t|
      t.string :title
      t.boolean :completionstatus
      t.string :text
      t.integer :user_id

      t.timestamps
    end
  end
end
