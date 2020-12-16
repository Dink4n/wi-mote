import React from "react";
import { AwesomeButton } from "react-awesome-button";
import { Grid } from "semantic-ui-react";
import {
	MdChevronLeft,
	MdChevronRight,
	MdExpandMore,
	MdExpandLess,
	MdPause
} from "react-icons/md"
import { handleKeyPress } from "../api";

export const Player = () => {
	return (
		<Grid columns="equal">
			<Grid.Row verticalAlign="top">
				<Grid.Column>
					<AwesomeButton
						size="small"
						type="secondary"
						onPress={() => handleKeyPress("up")}
					>
						<MdExpandLess size={20} />
					</AwesomeButton>
				</Grid.Column>
			</Grid.Row>
			<Grid.Row verticalAlign="middle">
				<Grid.Column>
					<AwesomeButton
						size="small"
						type="secondary"
						onPress={() => handleKeyPress("left")}
					>
						<MdChevronLeft size={20} />
					</AwesomeButton>
				</Grid.Column>
				<Grid.Column>
					<AwesomeButton
						size="small"
						type="secondary"
						onPress={() => handleKeyPress("playpause")}
					>
						<MdPause size={20} />
					</AwesomeButton>
				</Grid.Column>
				<Grid.Column>
					<AwesomeButton
						size="small"
						type="secondary"
						onPress={() => handleKeyPress("right")}
					>
						<MdChevronRight size={20} />
					</AwesomeButton>
				</Grid.Column>
			</Grid.Row>
			<Grid.Row verticalAlign="bottom">
				<Grid.Column>
					<AwesomeButton
						size="small"
						type="secondary"
						onPress={() => handleKeyPress("down")}
					>
						<MdExpandMore size={20} />
					</AwesomeButton>
				</Grid.Column>
			</Grid.Row>
		</Grid>
	);
};
