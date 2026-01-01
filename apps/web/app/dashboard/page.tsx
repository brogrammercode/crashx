"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { Plus, Loader2, Copy } from "lucide-react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";

import { Button } from "@/shared/components/ui/button";
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/shared/components/ui/card";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "@/shared/components/ui/dialog";
import { Input } from "@/shared/components/ui/input";
import { Label } from "@/shared/components/ui/label";
import { ApiProjectRepository } from "@/infrastructure/repositories/project.repository";
import { GetProjects } from "@/core/use-cases/get-projects";
import { CreateProject } from "@/core/use-cases/create-project";
import { Project } from "@/core/entities/project";

const projectSchema = z.object({
    name: z.string().min(1, "Project name is required"),
    discordWebhook: z.string().optional(),
});

export default function DashboardPage() {
    const router = useRouter();
    const [projects, setProjects] = useState<Project[]>([]);
    const [loading, setLoading] = useState(true);
    const [open, setOpen] = useState(false);
    const [creating, setCreating] = useState(false);

    const form = useForm<z.infer<typeof projectSchema>>({
        resolver: zodResolver(projectSchema),
    });

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (!token) {
            router.push("/login");
            return;
        }
        fetchProjects();
    }, [router]);

    async function fetchProjects() {
        try {
            const repo = new ApiProjectRepository();
            const useCase = new GetProjects(repo);
            const data = await useCase.execute();
            setProjects(data);
        } catch (error) {
            console.error("Failed to fetch projects", error);
        } finally {
            setLoading(false);
        }
    }

    async function onCreateProject(values: z.infer<typeof projectSchema>) {
        setCreating(true);
        try {
            const repo = new ApiProjectRepository();
            const useCase = new CreateProject(repo);
            await useCase.execute(values.name, values.discordWebhook);
            setOpen(false);
            form.reset();
            fetchProjects();
        } catch (error) {
            console.error("Failed to create project", error);
        } finally {
            setCreating(false);
        }
    }

    const copyToClipboard = (text: string) => {
        navigator.clipboard.writeText(text);
        alert("Copied to clipboard!");
    };

    if (loading) {
        return (
            <div className="flex h-screen w-full items-center justify-center">
                <Loader2 className="h-8 w-8 animate-spin text-primary" />
            </div>
        );
    }

    return (
        <div className="container mx-auto py-10">
            <div className="flex items-center justify-between mb-8">
                <div>
                    <h1 className="text-3xl font-bold tracking-tight">Dashboard</h1>
                    <p className="text-muted-foreground">
                        Manage your projects and API keys.
                    </p>
                </div>
                <Dialog open={open} onOpenChange={setOpen}>
                    <DialogTrigger asChild>
                        <Button>
                            <Plus className="mr-2 h-4 w-4" /> New Project
                        </Button>
                    </DialogTrigger>
                    <DialogContent>
                        <DialogHeader>
                            <DialogTitle>Create Project</DialogTitle>
                            <DialogDescription>
                                Create a new project to get an API key.
                            </DialogDescription>
                        </DialogHeader>
                        <form onSubmit={form.handleSubmit(onCreateProject)}>
                            <div className="grid gap-4 py-4">
                                <div className="grid gap-2">
                                    <Label htmlFor="name">Project Name</Label>
                                    <Input id="name" {...form.register("name")} />
                                    {form.formState.errors.name && (
                                        <span className="text-sm text-red-500">
                                            {form.formState.errors.name.message}
                                        </span>
                                    )}
                                </div>
                                <div className="grid gap-2">
                                    <Label htmlFor="discord">Discord Webhook (Optional)</Label>
                                    <Input
                                        id="discord"
                                        placeholder="https://discord.com/api/webhooks/..."
                                        {...form.register("discordWebhook")}
                                    />
                                </div>
                            </div>
                            <DialogFooter>
                                <Button type="submit" disabled={creating}>
                                    {creating ? "Creating..." : "Create Project"}
                                </Button>
                            </DialogFooter>
                        </form>
                    </DialogContent>
                </Dialog>
            </div>

            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
                {projects.length === 0 ? (
                    <div className="col-span-full text-center py-10 border rounded-lg bg-muted/20 border-dashed">
                        <p className="text-muted-foreground">
                            No projects found. Create one to get started.
                        </p>
                    </div>
                ) : (
                    projects.map((project) => (
                        <Card key={project.id}>
                            <CardHeader>
                                <CardTitle>{project.name}</CardTitle>
                                <CardDescription>Created just now</CardDescription>
                            </CardHeader>
                            <CardContent>
                                <div className="grid gap-2">
                                    <Label className="text-xs text-muted-foreground">
                                        API KEY
                                    </Label>
                                    <div className="flex items-center gap-2">
                                        <code className="relative rounded bg-muted px-[0.3rem] py-[0.2rem] font-mono text-sm flex-1 truncate">
                                            {project.apiKey}
                                        </code>
                                        <Button
                                            variant="ghost"
                                            size="icon"
                                            className="h-8 w-8"
                                            onClick={() => copyToClipboard(project.apiKey)}
                                        >
                                            <Copy className="h-4 w-4" />
                                        </Button>
                                    </div>
                                </div>
                            </CardContent>
                        </Card>
                    ))
                )}
            </div>
        </div>
    );
}
