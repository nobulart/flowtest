using Test, HTTP, JSON3, FilePaths
include("$REPO_PATH/app.jl")
@testset "Genie API" begin
response = HTTP.get("http://localhost:8000/hello")
@test response.status == 200
@test JSON3.read(response.body) == Dict("message" => "Hello, World!")
response = HTTP.get("http://localhost:8000/data")
@test response.status == 200
if isfile("$REPO_PATH/data.csv")
@test isa(JSON3.read(response.body), Vector)
else
@test JSON3.read(response.body) == Dict("error" => "Dataset not found")
end
end